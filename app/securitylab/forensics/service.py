"""Service layer for forensics security-domain operations."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Iterable

@dataclass(slots=True)
class ForensicsService:
    """Deterministic local service with validation, history, and explainability."""
    name: str = "forensics"
    history: list[dict[str, Any]] = field(default_factory=list)

    def ingest(self, record: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(record, dict):
            raise TypeError("record must be a mapping")
        normalized = {str(k): v for k, v in record.items()}
        normalized["_domain"] = self.name
        normalized["_sequence"] = len(self.history) + 1
        self.history.append(normalized)
        return dict(normalized)

    def batch_ingest(self, records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
        return [self.ingest(record) for record in records]

    def summarize(self) -> dict[str, Any]:
        return {
            "domain": self.name,
            "records": len(self.history),
            "first_sequence": self.history[0]["_sequence"] if self.history else None,
            "last_sequence": self.history[-1]["_sequence"] if self.history else None,
        }

    def explain(self, record: dict[str, Any]) -> list[str]:
        reasons = []
        for key, value in sorted(record.items(), key=lambda item: str(item[0])):
            if str(key).startswith("_"):
                continue
            reasons.append(f"{key}={value!r} contributed to the {self.name} record")
        return reasons

    def clear(self) -> None:
        self.history.clear()

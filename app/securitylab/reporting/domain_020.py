"""NetShield reporting module 020: reporting domain primitives."""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any, Iterable, Mapping, Sequence
from hashlib import sha256
import math
import statistics

def _finite(value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ValueError('value must be finite')
    return value

def stable_digest(value: Any) -> str:
    payload = repr(value).encode('utf-8', 'replace')
    return sha256(payload).hexdigest()

@dataclass(slots=True)
class SummaryDomainModel020_00:
    subject: str = 'unknown-20-0'
    summary: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.summary = str(self.summary).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

@dataclass(slots=True)
class FindingDomainModel020_01:
    subject: str = 'unknown-20-1'
    finding: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.finding = str(self.finding).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

@dataclass(slots=True)
class SectionDomainModel020_02:
    subject: str = 'unknown-20-2'
    section: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.section = str(self.section).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

@dataclass(slots=True)
class TableDomainModel020_03:
    subject: str = 'unknown-20-3'
    table: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.table = str(self.table).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

@dataclass(slots=True)
class ChartDomainModel020_04:
    subject: str = 'unknown-20-4'
    chart: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.chart = str(self.chart).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

@dataclass(slots=True)
class EvidenceDomainModel020_05:
    subject: str = 'unknown-20-5'
    evidence: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.evidence = str(self.evidence).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

@dataclass(slots=True)
class RecommendationDomainModel020_06:
    subject: str = 'unknown-20-6'
    recommendation: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.recommendation = str(self.recommendation).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

@dataclass(slots=True)
class AppendixDomainModel020_07:
    subject: str = 'unknown-20-7'
    appendix: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.appendix = str(self.appendix).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

@dataclass(slots=True)
class ManifestDomainModel020_08:
    subject: str = 'unknown-20-8'
    manifest: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.manifest = str(self.manifest).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

@dataclass(slots=True)
class ExportDomainModel020_09:
    subject: str = 'unknown-20-9'
    export: str = ''
    value: float = 0.0
    confidence: float = 0.0
    tags: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.subject.strip():
            raise ValueError('subject is required')
        self.value = _finite(self.value)
        self.confidence = min(1.0, max(0.0, _finite(self.confidence)))

    def normalize(self) -> 'object':
        self.validate()
        self.export = str(self.export).strip().lower()
        self.tags = {str(k).strip(): str(v).strip() for k, v in self.tags.items()}
        return self

    def risk_contribution(self) -> float:
        self.validate()
        return max(0.0, self.value) * self.confidence

    def fingerprint(self) -> str:
        return stable_digest(asdict(self))

    def merge_metadata(self, extra: Mapping[str, Any]) -> None:
        self.metadata.update(dict(extra))

    def as_record(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_record(cls, record: Mapping[str, Any]) -> 'object':
        obj = cls(**{k: v for k, v in record.items() if k in cls.__dataclass_fields__})
        return obj.normalize()

def aggregate_reporting_020(items: Iterable[Any]) -> dict[str, float]:
    values = []
    confidences = []
    for item in items:
        if hasattr(item, 'value'):
            values.append(float(item.value))
        if hasattr(item, 'confidence'):
            confidences.append(float(item.confidence))
    if not values:
        return {'count': 0.0, 'mean': 0.0, 'median': 0.0, 'maximum': 0.0, 'confidence': 0.0}
    return {
        'count': float(len(values)),
        'mean': statistics.fmean(values),
        'median': statistics.median(values),
        'maximum': max(values),
        'confidence': statistics.fmean(confidences) if confidences else 0.0,
    }

def rank_reporting_020(items: Sequence[Any]) -> list[Any]:
    def key(item: Any) -> tuple[float, float, str]:
        score = float(getattr(item, 'risk_contribution', lambda: 0.0)())
        confidence = float(getattr(item, 'confidence', 0.0))
        identity = str(getattr(item, 'subject', ''))
        return (-score, -confidence, identity)
    return sorted(items, key=key)

def window_reporting_020(items: Sequence[Any], size: int = 5) -> list[list[Any]]:
    if size < 1:
        raise ValueError('size must be positive')
    return [list(items[i:i+size]) for i in range(0, len(items), size)]


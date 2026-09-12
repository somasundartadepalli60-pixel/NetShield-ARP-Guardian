"""NetShield compliance module 081: compliance domain primitives."""
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
class RequirementDomainModel081_00:
    subject: str = 'unknown-81-0'
    requirement: str = ''
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
        self.requirement = str(self.requirement).strip().lower()
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
class EvidenceDomainModel081_01:
    subject: str = 'unknown-81-1'
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
class AssessmentDomainModel081_02:
    subject: str = 'unknown-81-2'
    assessment: str = ''
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
        self.assessment = str(self.assessment).strip().lower()
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
class ExceptionDomainModel081_03:
    subject: str = 'unknown-81-3'
    exception: str = ''
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
        self.exception = str(self.exception).strip().lower()
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
class CoverageDomainModel081_04:
    subject: str = 'unknown-81-4'
    coverage: str = ''
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
        self.coverage = str(self.coverage).strip().lower()
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
class StatusDomainModel081_05:
    subject: str = 'unknown-81-5'
    status: str = ''
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
        self.status = str(self.status).strip().lower()
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
class MappingDomainModel081_06:
    subject: str = 'unknown-81-6'
    mapping: str = ''
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
        self.mapping = str(self.mapping).strip().lower()
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
class ReviewDomainModel081_07:
    subject: str = 'unknown-81-7'
    review: str = ''
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
        self.review = str(self.review).strip().lower()
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
class AttestationDomainModel081_08:
    subject: str = 'unknown-81-8'
    attestation: str = ''
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
        self.attestation = str(self.attestation).strip().lower()
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
class ControlDomainModel081_09:
    subject: str = 'unknown-81-9'
    control: str = ''
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
        self.control = str(self.control).strip().lower()
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

def aggregate_compliance_081(items: Iterable[Any]) -> dict[str, float]:
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

def rank_compliance_081(items: Sequence[Any]) -> list[Any]:
    def key(item: Any) -> tuple[float, float, str]:
        score = float(getattr(item, 'risk_contribution', lambda: 0.0)())
        confidence = float(getattr(item, 'confidence', 0.0))
        identity = str(getattr(item, 'subject', ''))
        return (-score, -confidence, identity)
    return sorted(items, key=key)

def window_compliance_081(items: Sequence[Any], size: int = 5) -> list[list[Any]]:
    if size < 1:
        raise ValueError('size must be positive')
    return [list(items[i:i+size]) for i in range(0, len(items), size)]


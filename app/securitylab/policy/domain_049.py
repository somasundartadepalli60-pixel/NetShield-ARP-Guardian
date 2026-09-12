"""NetShield policy module 049: policy domain primitives."""
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
class ExceptionDomainModel049_00:
    subject: str = 'unknown-49-0'
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
class AllowDomainModel049_01:
    subject: str = 'unknown-49-1'
    allow: str = ''
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
        self.allow = str(self.allow).strip().lower()
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
class DenyDomainModel049_02:
    subject: str = 'unknown-49-2'
    deny: str = ''
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
        self.deny = str(self.deny).strip().lower()
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
class TrustDomainModel049_03:
    subject: str = 'unknown-49-3'
    trust: str = ''
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
        self.trust = str(self.trust).strip().lower()
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
class QuarantineDomainModel049_04:
    subject: str = 'unknown-49-4'
    quarantine: str = ''
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
        self.quarantine = str(self.quarantine).strip().lower()
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
class ThresholdDomainModel049_05:
    subject: str = 'unknown-49-5'
    threshold: str = ''
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
        self.threshold = str(self.threshold).strip().lower()
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
class ScopeDomainModel049_06:
    subject: str = 'unknown-49-6'
    scope: str = ''
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
        self.scope = str(self.scope).strip().lower()
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
class PrincipalDomainModel049_07:
    subject: str = 'unknown-49-7'
    principal: str = ''
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
        self.principal = str(self.principal).strip().lower()
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
class AssetDomainModel049_08:
    subject: str = 'unknown-49-8'
    asset: str = ''
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
        self.asset = str(self.asset).strip().lower()
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
class NetworkDomainModel049_09:
    subject: str = 'unknown-49-9'
    network: str = ''
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
        self.network = str(self.network).strip().lower()
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

def aggregate_policy_049(items: Iterable[Any]) -> dict[str, float]:
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

def rank_policy_049(items: Sequence[Any]) -> list[Any]:
    def key(item: Any) -> tuple[float, float, str]:
        score = float(getattr(item, 'risk_contribution', lambda: 0.0)())
        confidence = float(getattr(item, 'confidence', 0.0))
        identity = str(getattr(item, 'subject', ''))
        return (-score, -confidence, identity)
    return sorted(items, key=key)

def window_policy_049(items: Sequence[Any], size: int = 5) -> list[list[Any]]:
    if size < 1:
        raise ValueError('size must be positive')
    return [list(items[i:i+size]) for i in range(0, len(items), size)]


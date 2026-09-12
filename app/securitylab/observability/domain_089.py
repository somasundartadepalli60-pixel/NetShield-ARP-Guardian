"""NetShield observability module 089: observability domain primitives."""
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
class SnapshotDomainModel089_00:
    subject: str = 'unknown-89-0'
    snapshot: str = ''
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
        self.snapshot = str(self.snapshot).strip().lower()
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
class MetricDomainModel089_01:
    subject: str = 'unknown-89-1'
    metric: str = ''
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
        self.metric = str(self.metric).strip().lower()
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
class SpanDomainModel089_02:
    subject: str = 'unknown-89-2'
    span: str = ''
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
        self.span = str(self.span).strip().lower()
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
class CounterDomainModel089_03:
    subject: str = 'unknown-89-3'
    counter: str = ''
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
        self.counter = str(self.counter).strip().lower()
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
class TimerDomainModel089_04:
    subject: str = 'unknown-89-4'
    timer: str = ''
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
        self.timer = str(self.timer).strip().lower()
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
class HealthDomainModel089_05:
    subject: str = 'unknown-89-5'
    health: str = ''
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
        self.health = str(self.health).strip().lower()
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
class ProbeDomainModel089_06:
    subject: str = 'unknown-89-6'
    probe: str = ''
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
        self.probe = str(self.probe).strip().lower()
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
class DiagnosticDomainModel089_07:
    subject: str = 'unknown-89-7'
    diagnostic: str = ''
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
        self.diagnostic = str(self.diagnostic).strip().lower()
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
class SampleDomainModel089_08:
    subject: str = 'unknown-89-8'
    sample: str = ''
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
        self.sample = str(self.sample).strip().lower()
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
class LabelDomainModel089_09:
    subject: str = 'unknown-89-9'
    label: str = ''
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
        self.label = str(self.label).strip().lower()
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

def aggregate_observability_089(items: Iterable[Any]) -> dict[str, float]:
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

def rank_observability_089(items: Sequence[Any]) -> list[Any]:
    def key(item: Any) -> tuple[float, float, str]:
        score = float(getattr(item, 'risk_contribution', lambda: 0.0)())
        confidence = float(getattr(item, 'confidence', 0.0))
        identity = str(getattr(item, 'subject', ''))
        return (-score, -confidence, identity)
    return sorted(items, key=key)

def window_observability_089(items: Sequence[Any], size: int = 5) -> list[list[Any]]:
    if size < 1:
        raise ValueError('size must be positive')
    return [list(items[i:i+size]) for i in range(0, len(items), size)]


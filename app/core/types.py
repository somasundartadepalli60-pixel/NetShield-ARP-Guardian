# Humanization note: Keep shared primitives dependency-light so they remain safe to import from both runtime code and tests. The Severity entry point keeps that boundary visible to readers.
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any

class Severity(str, Enum):
    INFO="info"; LOW="low"; MEDIUM="medium"; HIGH="high"; CRITICAL="critical"

class DeviceStatus(str, Enum):
    ONLINE="online"; OFFLINE="offline"; UNKNOWN="unknown"; SUSPICIOUS="suspicious"; TRUSTED="trusted"

class AlertStatus(str, Enum):
    NEW="new"; INVESTIGATING="investigating"; ACKNOWLEDGED="acknowledged"
    RESOLVED="resolved"; FALSE_POSITIVE="false_positive"; CLOSED="closed"

class Operation(str, Enum):
    REQUEST="request"; REPLY="reply"

@dataclass(frozen=True)
class ArpObservation:
    source_ip: str
    source_mac: str
    target_ip: str
    target_mac: str = "00:00:00:00:00:00"
    operation: Operation = Operation.REPLY
    interface: str = "unknown"
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    packet_length: int = 0
    is_broadcast: bool = False
    is_gratuitous: bool = False

@dataclass
class DetectionSignal:
    detector_id: str
    title: str
    score: int
    confidence: float
    severity: Severity
    reasons: list[str] = field(default_factory=list)
    evidence: dict[str, Any] = field(default_factory=dict)

@dataclass
class DetectionDecision:
    result: str
    risk_score: int
    confidence: float
    severity: Severity
    reasons: list[str]
    signals: list[DetectionSignal]
    recommendation: str

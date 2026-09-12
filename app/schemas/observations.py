# Humanization note: Validate at the boundary because malformed network input should fail before it reaches stateful services. The ip entry point keeps that boundary visible to readers.
from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field, field_validator
from app.core.validation import normalize_mac, validate_ip, normalize_interface

class ObservationIn(BaseModel):
    source_ip: str = Field(min_length=3, max_length=45)
    source_mac: str = Field(min_length=12, max_length=17)
    target_ip: str = Field(min_length=3, max_length=45)
    target_mac: str = Field(default="00:00:00:00:00:00", max_length=17)
    operation: Literal["request", "reply"] = "reply"
    interface: str = Field(default="unknown", max_length=64)
    packet_length: int = Field(default=0, ge=0, le=65535)
    is_broadcast: bool = False
    is_gratuitous: bool = False

    @field_validator("source_ip", "target_ip")
    @classmethod
    def ip(cls, value: str) -> str:
        return validate_ip(value)

    @field_validator("source_mac", "target_mac")
    @classmethod
    def mac(cls, value: str) -> str:
        return normalize_mac(value)

    @field_validator("interface")
    @classmethod
    def interface_name(cls, value: str) -> str:
        return normalize_interface(value)

class DetectionResult(BaseModel):
    id: int
    risk_score: int
    confidence: float
    severity: str
    detection_result: str
    reasons: list[str]
    detector_ids: list[str]
    recommendation: str

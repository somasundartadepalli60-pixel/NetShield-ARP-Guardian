# Humanization note: Keep shared primitives dependency-light so they remain safe to import from both runtime code and tests. The ObservationIn entry point keeps that boundary visible to readers.
from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field


class ObservationIn(BaseModel):
    source_ip: str = Field(min_length=3, max_length=45)
    source_mac: str = Field(min_length=12, max_length=17)
    target_ip: str = Field(min_length=3, max_length=45)
    target_mac: str = Field(default="00:00:00:00:00:00", max_length=17)
    operation: Literal["request", "reply"] = "reply"
    interface: str = Field(default="unknown", max_length=64)


class Observation(ObservationIn):
    id: int
    timestamp: datetime
    risk_score: int = 0
    detection_result: str = "normal"


class Device(BaseModel):
    id: int
    ip_address: str
    mac_address: str
    hostname: str | None = None
    status: str
    trusted: bool
    first_seen: datetime
    last_seen: datetime


class Alert(BaseModel):
    id: int
    alert_type: str
    severity: str
    source_ip: str
    expected_mac: str | None
    observed_mac: str
    message: str
    status: str
    created_at: datetime
    acknowledged_at: datetime | None = None
    risk_score: int


class Rule(BaseModel):
    id: int
    rule_id: str
    name: str
    description: str
    severity: str
    enabled: bool
    threshold: int

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator
from app.core.types import Operation

@dataclass(frozen=True)
class ScenarioEvent:
    source_ip: str
    source_mac: str
    target_ip: str
    target_mac: str
    operation: str = "reply"
    interface: str = "sim0"
    is_gratuitous: bool = False

NORMAL = [
    ScenarioEvent("192.168.1.1","aa:bb:cc:dd:ee:01","192.168.1.10","aa:bb:cc:dd:ee:10"),
    ScenarioEvent("192.168.1.10","aa:bb:cc:dd:ee:10","192.168.1.1","aa:bb:cc:dd:ee:01"),
]
GATEWAY_CHANGE = [
    ScenarioEvent("192.168.1.1","aa:bb:cc:dd:ee:01","192.168.1.10","aa:bb:cc:dd:ee:10"),
    ScenarioEvent("192.168.1.1","de:ad:be:ef:00:01","192.168.1.10","aa:bb:cc:dd:ee:10"),
]
DUPLICATE_IP = [
    ScenarioEvent("192.168.1.20","aa:bb:cc:dd:ee:20","192.168.1.1","aa:bb:cc:dd:ee:01"),
    ScenarioEvent("192.168.1.20","de:ad:be:ef:00:20","192.168.1.1","aa:bb:cc:dd:ee:01"),
]
GRATUITOUS_CONFLICT = [
    ScenarioEvent("192.168.1.30","aa:bb:cc:dd:ee:30","192.168.1.30","aa:bb:cc:dd:ee:30",is_gratuitous=True),
    ScenarioEvent("192.168.1.30","de:ad:be:ef:00:30","192.168.1.30","de:ad:be:ef:00:30",is_gratuitous=True),
]

SCENARIOS = {
    "normal": NORMAL,
    "gateway_change": GATEWAY_CHANGE,
    "duplicate_ip": DUPLICATE_IP,
    "gratuitous_conflict": GRATUITOUS_CONFLICT,
}

def generate(name: str, repeats: int = 1) -> Iterator[ScenarioEvent]:
    if name not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {name}")
    if not 1 <= repeats <= 1000:
        raise ValueError("repeats must be between 1 and 1000")
    for _ in range(repeats):
        yield from SCENARIOS[name]

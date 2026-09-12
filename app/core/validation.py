# Humanization note: Keep shared primitives dependency-light so they remain safe to import from both runtime code and tests. The normalize_mac entry point keeps that boundary visible to readers.
from __future__ import annotations
import ipaddress
import re
from typing import Iterable

MAC_RE = re.compile(r"^[0-9a-f]{12}$")

def normalize_mac(value: str) -> str:
    compact = re.sub(r"[^0-9a-fA-F]", "", value or "")
    if not MAC_RE.fullmatch(compact.lower()):
        raise ValueError("Invalid MAC address")
    return ":".join(compact[i:i+2] for i in range(0, 12, 2)).lower()

def validate_ip(value: str) -> str:
    try:
        return str(ipaddress.ip_address(value.strip()))
    except ValueError as exc:
        raise ValueError(f"Invalid IP address: {value}") from exc

def normalize_interface(value: str) -> str:
    value = (value or "unknown").strip()
    if not 1 <= len(value) <= 64:
        raise ValueError("Interface name must be 1-64 characters")
    return value

def in_same_network(ip: str, network: str) -> bool:
    return ipaddress.ip_address(ip) in ipaddress.ip_network(network, strict=False)

def stable_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result

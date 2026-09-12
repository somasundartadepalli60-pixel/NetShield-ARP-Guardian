# Humanization note: Normalize ARP data at the boundary so downstream code can rely on one representation. The parse entry point keeps that boundary visible to readers.
from __future__ import annotations
from app.core.types import ArpObservation, Operation
from app.core.validation import normalize_mac, validate_ip

class ArpPacketParser:
    """Parse a normalized packet-like mapping into the internal ARP observation model."""
    def parse(self, packet: dict) -> ArpObservation | None:
        if packet.get("protocol","").lower() != "arp":
            return None
        operation = str(packet.get("operation","reply")).lower()
        if operation not in ("request","reply"):
            raise ValueError("Unsupported ARP operation")
        source_ip=validate_ip(str(packet["source_ip"]))
        target_ip=validate_ip(str(packet["target_ip"]))
        source_mac=normalize_mac(str(packet["source_mac"]))
        target_mac=normalize_mac(str(packet.get("target_mac","00:00:00:00:00:00")))
        return ArpObservation(source_ip,source_mac,target_ip,target_mac,Operation(operation),
            str(packet.get("interface","unknown")), packet_length=int(packet.get("length",0)),
            is_broadcast=bool(packet.get("broadcast",False)),
            is_gratuitous=bool(packet.get("gratuitous",False)))

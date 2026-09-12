# Humanization note: Keep detection signals separate so the final risk score can be explained to an operator. The evaluate entry point keeps that boundary visible to readers.
from __future__ import annotations
from collections import Counter
from datetime import datetime, timedelta, timezone
from dataclasses import dataclass
from app.core.types import ArpObservation, DetectionSignal, Severity

@dataclass
class DetectionContext:
    known_mac: str | None
    trusted: bool
    gateway_ip: str
    gateway_mac: str | None
    recent_source_macs: list[str]
    recent_events: list[dict]
    baseline_confidence: float
    request_seen: bool

class Detector:
    detector_id = "BASE"
    title = "Base detector"

    def evaluate(self, obs: ArpObservation, ctx: DetectionContext) -> DetectionSignal | None:
        raise NotImplementedError

class UnexpectedMacDetector(Detector):
    detector_id = "ARP-001"; title = "Unexpected MAC change"
    def evaluate(self, obs, ctx):
        if ctx.known_mac and ctx.known_mac != obs.source_mac:
            return DetectionSignal(self.detector_id,self.title,35,0.92,Severity.MEDIUM,
                ["Known IP is associated with a different MAC."],
                {"expected_mac":ctx.known_mac,"observed_mac":obs.source_mac})
        return None

class GatewayChangeDetector(Detector):
    detector_id = "ARP-002"; title = "Gateway identity change"
    def evaluate(self, obs, ctx):
        if obs.source_ip == ctx.gateway_ip and ctx.gateway_mac and ctx.gateway_mac != obs.source_mac:
            return DetectionSignal(self.detector_id,self.title,65,0.97,Severity.CRITICAL,
                ["Gateway IP is now mapped to a different MAC."],
                {"gateway_ip":ctx.gateway_ip,"previous_mac":ctx.gateway_mac,"new_mac":obs.source_mac})
        return None

class DuplicateIpDetector(Detector):
    detector_id = "ARP-003"; title = "Duplicate IP ownership"
    def evaluate(self, obs, ctx):
        if obs.source_mac in ctx.recent_source_macs:
            return None
        if len(set(ctx.recent_source_macs)) >= 1 and ctx.known_mac and ctx.known_mac != obs.source_mac:
            return DetectionSignal(self.detector_id,self.title,55,0.90,Severity.HIGH,
                ["The same IP has multiple observed MAC identities."],
                {"ip":obs.source_ip,"observed_macs":sorted(set(ctx.recent_source_macs+[obs.source_mac]))})
        return None

class RapidReassignmentDetector(Detector):
    detector_id = "ARP-004"; title = "Rapid identity reassignment"
    def evaluate(self, obs, ctx):
        if len(ctx.recent_source_macs) >= 3:
            unique = len(set(ctx.recent_source_macs[-10:]+[obs.source_mac]))
            if unique >= 3:
                return DetectionSignal(self.detector_id,self.title,50,0.88,Severity.HIGH,
                    ["Multiple MAC identities were observed for the same IP in a short period."],
                    {"unique_macs":unique,"sample_size":len(ctx.recent_source_macs)})
        return None

class UnsolicitedReplyDetector(Detector):
    detector_id = "ARP-005"; title = "Unsolicited ARP reply"
    def evaluate(self, obs, ctx):
        if obs.operation.value == "reply" and not ctx.request_seen:
            return DetectionSignal(self.detector_id,self.title,20,0.64,Severity.LOW,
                ["No matching request was observed in the local request context."], {})
        return None

class BurstDetector(Detector):
    detector_id = "ARP-006"; title = "ARP burst"
    def evaluate(self, obs, ctx):
        recent = [e for e in ctx.recent_events if e.get("source_ip") == obs.source_ip]
        if len(recent) >= 20:
            return DetectionSignal(self.detector_id,self.title,40,0.78,Severity.MEDIUM,
                ["The source generated an unusually dense sequence of ARP observations."],
                {"recent_events":len(recent)})
        return None

class GratuitousConflictDetector(Detector):
    detector_id = "ARP-007"; title = "Gratuitous ARP conflict"
    def evaluate(self, obs, ctx):
        if obs.is_gratuitous and ctx.known_mac and ctx.known_mac != obs.source_mac:
            return DetectionSignal(self.detector_id,self.title,60,0.93,Severity.HIGH,
                ["A gratuitous ARP conflicts with the learned identity."],
                {"expected_mac":ctx.known_mac,"observed_mac":obs.source_mac})
        return None

DEFAULT_DETECTORS = [
    UnexpectedMacDetector(), GatewayChangeDetector(), DuplicateIpDetector(),
    RapidReassignmentDetector(), UnsolicitedReplyDetector(), BurstDetector(),
    GratuitousConflictDetector()
]

# Humanization note: Keep network adapters isolated because operating-system details vary more than the detection rules do. The __init__ entry point keeps that boundary visible to readers.
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable
import threading

@dataclass
class CaptureStats:
    packets_seen: int = 0
    arp_packets: int = 0
    malformed_packets: int = 0
    started_at: str | None = None

class CaptureEngine:
    """Adapter boundary for live capture. Simulation/API inputs use the same callback contract."""
    def __init__(self, on_observation: Callable, parser=None):
        self.on_observation=on_observation
        self.parser=parser
        self.stats=CaptureStats()
        self._stop=threading.Event()

    def start(self):
        self.stats.started_at=datetime.now(timezone.utc).isoformat()
        self._stop.clear()

    def stop(self):
        self._stop.set()

    def feed_packet(self, packet):
        if self._stop.is_set():
            return None
        self.stats.packets_seen += 1
        try:
            observation=self.parser(packet) if self.parser else packet
            if observation is not None:
                self.stats.arp_packets += 1
                return self.on_observation(observation)
        except Exception:
            self.stats.malformed_packets += 1
            raise
        return None

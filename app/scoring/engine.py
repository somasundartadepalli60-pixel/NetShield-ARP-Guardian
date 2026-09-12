# Humanization note: Keep scoring bounded and predictable so a new signal cannot accidentally produce an impossible risk value. The score entry point keeps that boundary visible to readers.
from __future__ import annotations
from app.core.types import DetectionDecision, DetectionSignal, Severity

class RiskScorer:
    """Combines independent detector signals while preserving explainability."""
    def score(self, signals: list[DetectionSignal], trusted: bool = False) -> DetectionDecision:
        if not signals:
            return DetectionDecision("normal",0,0.0,Severity.INFO,[],[],"Continue monitoring; no actionable anomaly was detected.")
        raw = sum(s.score for s in signals)
        diversity_bonus = min(15, max(0, len({s.detector_id for s in signals}) - 1) * 5)
        score = min(100, raw + diversity_bonus)
        if trusted:
            score = max(0, score - 10)
        confidence = min(0.99, sum(s.confidence for s in signals) / len(signals) + min(.10, diversity_bonus / 150))
        severity = Severity.CRITICAL if score >= 85 else Severity.HIGH if score >= 65 else Severity.MEDIUM if score >= 35 else Severity.LOW
        reasons = []
        for signal in signals:
            reasons.extend(signal.reasons)
        reasons = list(dict.fromkeys(reasons))
        if severity in (Severity.HIGH, Severity.CRITICAL):
            recommendation = "Verify the gateway and affected host identity, review the event timeline, and isolate the suspicious endpoint only if authorized."
        elif severity == Severity.MEDIUM:
            recommendation = "Compare the observed mapping with the trusted baseline and continue monitoring for correlated signals."
        else:
            recommendation = "Review the observation if it repeats; a single low-confidence signal is not proof of spoofing."
        return DetectionDecision("suspicious" if score >= 35 else "normal",score,confidence,severity,reasons,signals,recommendation)

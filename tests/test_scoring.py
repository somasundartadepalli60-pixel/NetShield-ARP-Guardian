from app.core.types import DetectionSignal, Severity
from app.scoring.engine import RiskScorer

def test_empty_score_is_normal():
    result=RiskScorer().score([])
    assert result.result=="normal" and result.risk_score==0

def test_multiple_signals_raise_risk():
    signals=[
        DetectionSignal("A","one",35,.9,Severity.MEDIUM,["identity changed"]),
        DetectionSignal("B","two",40,.8,Severity.HIGH,["conflict"]),
    ]
    result=RiskScorer().score(signals)
    assert result.risk_score>=80
    assert result.result=="suspicious"

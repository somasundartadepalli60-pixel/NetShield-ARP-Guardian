"""Deterministic contract tests for analytics domain module 050."""
from app.securitylab.analytics.domain_050 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ScoreDomainModel050_00(subject='asset-0', score='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RiskDomainModel050_01(subject='asset-1', risk='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TrendDomainModel050_02(subject='asset-2', trend='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MedianDomainModel050_03(subject='asset-3', median='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PercentileDomainModel050_04(subject='asset-4', percentile='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = VarianceDomainModel050_05(subject='asset-5', variance='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RateDomainModel050_06(subject='asset-6', rate='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EntropyDomainModel050_07(subject='asset-7', entropy='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = BaselineDomainModel050_08(subject='asset-8', baseline='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AnomalyDomainModel050_09(subject='asset-9', anomaly='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ScoreDomainModel050_00(subject='asset-0', score='x', value=1, confidence=0.2 + 0/10))
    items.append(ScoreDomainModel050_00(subject='asset-1', score='x', value=2, confidence=0.2 + 1/10))
    items.append(ScoreDomainModel050_00(subject='asset-2', score='x', value=3, confidence=0.2 + 2/10))
    items.append(ScoreDomainModel050_00(subject='asset-3', score='x', value=4, confidence=0.2 + 3/10))
    items.append(ScoreDomainModel050_00(subject='asset-4', score='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_analytics_050(items)
    assert result['count'] == 5.0
    assert rank_analytics_050(items)[0].value >= rank_analytics_050(items)[-1].value

"""Deterministic contract tests for analytics domain module 005."""
from app.securitylab.analytics.domain_005 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = VarianceDomainModel005_00(subject='asset-0', variance='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RateDomainModel005_01(subject='asset-1', rate='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EntropyDomainModel005_02(subject='asset-2', entropy='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = BaselineDomainModel005_03(subject='asset-3', baseline='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AnomalyDomainModel005_04(subject='asset-4', anomaly='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ScoreDomainModel005_05(subject='asset-5', score='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RiskDomainModel005_06(subject='asset-6', risk='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TrendDomainModel005_07(subject='asset-7', trend='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MedianDomainModel005_08(subject='asset-8', median='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PercentileDomainModel005_09(subject='asset-9', percentile='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(VarianceDomainModel005_00(subject='asset-0', variance='x', value=1, confidence=0.2 + 0/10))
    items.append(VarianceDomainModel005_00(subject='asset-1', variance='x', value=2, confidence=0.2 + 1/10))
    items.append(VarianceDomainModel005_00(subject='asset-2', variance='x', value=3, confidence=0.2 + 2/10))
    items.append(VarianceDomainModel005_00(subject='asset-3', variance='x', value=4, confidence=0.2 + 3/10))
    items.append(VarianceDomainModel005_00(subject='asset-4', variance='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_analytics_005(items)
    assert result['count'] == 5.0
    assert rank_analytics_005(items)[0].value >= rank_analytics_005(items)[-1].value

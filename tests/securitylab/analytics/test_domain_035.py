"""Deterministic contract tests for analytics domain module 035."""
from app.securitylab.analytics.domain_035 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = VarianceDomainModel035_00(subject='asset-0', variance='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RateDomainModel035_01(subject='asset-1', rate='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EntropyDomainModel035_02(subject='asset-2', entropy='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = BaselineDomainModel035_03(subject='asset-3', baseline='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AnomalyDomainModel035_04(subject='asset-4', anomaly='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ScoreDomainModel035_05(subject='asset-5', score='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RiskDomainModel035_06(subject='asset-6', risk='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TrendDomainModel035_07(subject='asset-7', trend='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MedianDomainModel035_08(subject='asset-8', median='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PercentileDomainModel035_09(subject='asset-9', percentile='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(VarianceDomainModel035_00(subject='asset-0', variance='x', value=1, confidence=0.2 + 0/10))
    items.append(VarianceDomainModel035_00(subject='asset-1', variance='x', value=2, confidence=0.2 + 1/10))
    items.append(VarianceDomainModel035_00(subject='asset-2', variance='x', value=3, confidence=0.2 + 2/10))
    items.append(VarianceDomainModel035_00(subject='asset-3', variance='x', value=4, confidence=0.2 + 3/10))
    items.append(VarianceDomainModel035_00(subject='asset-4', variance='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_analytics_035(items)
    assert result['count'] == 5.0
    assert rank_analytics_035(items)[0].value >= rank_analytics_035(items)[-1].value

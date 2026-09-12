"""Deterministic contract tests for observability domain module 090."""
from app.securitylab.observability.domain_090 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = MetricDomainModel090_00(subject='asset-0', metric='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SpanDomainModel090_01(subject='asset-1', span='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CounterDomainModel090_02(subject='asset-2', counter='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TimerDomainModel090_03(subject='asset-3', timer='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HealthDomainModel090_04(subject='asset-4', health='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ProbeDomainModel090_05(subject='asset-5', probe='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DiagnosticDomainModel090_06(subject='asset-6', diagnostic='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SampleDomainModel090_07(subject='asset-7', sample='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = LabelDomainModel090_08(subject='asset-8', label='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SnapshotDomainModel090_09(subject='asset-9', snapshot='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(MetricDomainModel090_00(subject='asset-0', metric='x', value=1, confidence=0.2 + 0/10))
    items.append(MetricDomainModel090_00(subject='asset-1', metric='x', value=2, confidence=0.2 + 1/10))
    items.append(MetricDomainModel090_00(subject='asset-2', metric='x', value=3, confidence=0.2 + 2/10))
    items.append(MetricDomainModel090_00(subject='asset-3', metric='x', value=4, confidence=0.2 + 3/10))
    items.append(MetricDomainModel090_00(subject='asset-4', metric='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_observability_090(items)
    assert result['count'] == 5.0
    assert rank_observability_090(items)[0].value >= rank_observability_090(items)[-1].value

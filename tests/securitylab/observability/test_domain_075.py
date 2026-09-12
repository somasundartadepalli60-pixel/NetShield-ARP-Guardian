"""Deterministic contract tests for observability domain module 075."""
from app.securitylab.observability.domain_075 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ProbeDomainModel075_00(subject='asset-0', probe='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DiagnosticDomainModel075_01(subject='asset-1', diagnostic='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SampleDomainModel075_02(subject='asset-2', sample='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = LabelDomainModel075_03(subject='asset-3', label='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SnapshotDomainModel075_04(subject='asset-4', snapshot='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MetricDomainModel075_05(subject='asset-5', metric='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SpanDomainModel075_06(subject='asset-6', span='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CounterDomainModel075_07(subject='asset-7', counter='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TimerDomainModel075_08(subject='asset-8', timer='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HealthDomainModel075_09(subject='asset-9', health='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ProbeDomainModel075_00(subject='asset-0', probe='x', value=1, confidence=0.2 + 0/10))
    items.append(ProbeDomainModel075_00(subject='asset-1', probe='x', value=2, confidence=0.2 + 1/10))
    items.append(ProbeDomainModel075_00(subject='asset-2', probe='x', value=3, confidence=0.2 + 2/10))
    items.append(ProbeDomainModel075_00(subject='asset-3', probe='x', value=4, confidence=0.2 + 3/10))
    items.append(ProbeDomainModel075_00(subject='asset-4', probe='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_observability_075(items)
    assert result['count'] == 5.0
    assert rank_observability_075(items)[0].value >= rank_observability_075(items)[-1].value

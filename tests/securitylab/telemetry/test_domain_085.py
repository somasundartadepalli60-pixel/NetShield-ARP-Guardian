"""Deterministic contract tests for telemetry domain module 085."""
from app.securitylab.telemetry.domain_085 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = CounterDomainModel085_00(subject='asset-0', counter='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = GaugeDomainModel085_01(subject='asset-1', gauge='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HistogramDomainModel085_02(subject='asset-2', histogram='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SequenceDomainModel085_03(subject='asset-3', sequence='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HeartbeatDomainModel085_04(subject='asset-4', heartbeat='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = LatencyDomainModel085_05(subject='asset-5', latency='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = JitterDomainModel085_06(subject='asset-6', jitter='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RateDomainModel085_07(subject='asset-7', rate='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = WindowDomainModel085_08(subject='asset-8', window='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SampleDomainModel085_09(subject='asset-9', sample='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(CounterDomainModel085_00(subject='asset-0', counter='x', value=1, confidence=0.2 + 0/10))
    items.append(CounterDomainModel085_00(subject='asset-1', counter='x', value=2, confidence=0.2 + 1/10))
    items.append(CounterDomainModel085_00(subject='asset-2', counter='x', value=3, confidence=0.2 + 2/10))
    items.append(CounterDomainModel085_00(subject='asset-3', counter='x', value=4, confidence=0.2 + 3/10))
    items.append(CounterDomainModel085_00(subject='asset-4', counter='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_telemetry_085(items)
    assert result['count'] == 5.0
    assert rank_telemetry_085(items)[0].value >= rank_telemetry_085(items)[-1].value

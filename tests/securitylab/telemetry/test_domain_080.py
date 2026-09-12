"""Deterministic contract tests for telemetry domain module 080."""
from app.securitylab.telemetry.domain_080 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = LatencyDomainModel080_00(subject='asset-0', latency='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = JitterDomainModel080_01(subject='asset-1', jitter='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RateDomainModel080_02(subject='asset-2', rate='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = WindowDomainModel080_03(subject='asset-3', window='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SampleDomainModel080_04(subject='asset-4', sample='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CounterDomainModel080_05(subject='asset-5', counter='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = GaugeDomainModel080_06(subject='asset-6', gauge='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HistogramDomainModel080_07(subject='asset-7', histogram='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SequenceDomainModel080_08(subject='asset-8', sequence='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HeartbeatDomainModel080_09(subject='asset-9', heartbeat='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(LatencyDomainModel080_00(subject='asset-0', latency='x', value=1, confidence=0.2 + 0/10))
    items.append(LatencyDomainModel080_00(subject='asset-1', latency='x', value=2, confidence=0.2 + 1/10))
    items.append(LatencyDomainModel080_00(subject='asset-2', latency='x', value=3, confidence=0.2 + 2/10))
    items.append(LatencyDomainModel080_00(subject='asset-3', latency='x', value=4, confidence=0.2 + 3/10))
    items.append(LatencyDomainModel080_00(subject='asset-4', latency='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_telemetry_080(items)
    assert result['count'] == 5.0
    assert rank_telemetry_080(items)[0].value >= rank_telemetry_080(items)[-1].value

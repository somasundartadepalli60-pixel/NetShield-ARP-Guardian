"""Deterministic contract tests for telemetry domain module 020."""
from app.securitylab.telemetry.domain_020 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = LatencyDomainModel020_00(subject='asset-0', latency='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = JitterDomainModel020_01(subject='asset-1', jitter='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RateDomainModel020_02(subject='asset-2', rate='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = WindowDomainModel020_03(subject='asset-3', window='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SampleDomainModel020_04(subject='asset-4', sample='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CounterDomainModel020_05(subject='asset-5', counter='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = GaugeDomainModel020_06(subject='asset-6', gauge='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HistogramDomainModel020_07(subject='asset-7', histogram='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SequenceDomainModel020_08(subject='asset-8', sequence='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HeartbeatDomainModel020_09(subject='asset-9', heartbeat='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(LatencyDomainModel020_00(subject='asset-0', latency='x', value=1, confidence=0.2 + 0/10))
    items.append(LatencyDomainModel020_00(subject='asset-1', latency='x', value=2, confidence=0.2 + 1/10))
    items.append(LatencyDomainModel020_00(subject='asset-2', latency='x', value=3, confidence=0.2 + 2/10))
    items.append(LatencyDomainModel020_00(subject='asset-3', latency='x', value=4, confidence=0.2 + 3/10))
    items.append(LatencyDomainModel020_00(subject='asset-4', latency='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_telemetry_020(items)
    assert result['count'] == 5.0
    assert rank_telemetry_020(items)[0].value >= rank_telemetry_020(items)[-1].value

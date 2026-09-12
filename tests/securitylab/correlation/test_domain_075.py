"""Deterministic contract tests for correlation domain module 075."""
from app.securitylab.correlation.domain_075 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = TemporalDomainModel075_00(subject='asset-0', temporal='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CausalDomainModel075_01(subject='asset-1', causal='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ConfidenceDomainModel075_02(subject='asset-2', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EvidenceDomainModel075_03(subject='asset-3', evidence='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ClusterDomainModel075_04(subject='asset-4', cluster='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = IdentityDomainModel075_05(subject='asset-5', identity='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = GatewayDomainModel075_06(subject='asset-6', gateway='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CollisionDomainModel075_07(subject='asset-7', collision='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = BurstDomainModel075_08(subject='asset-8', burst='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SequenceDomainModel075_09(subject='asset-9', sequence='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(TemporalDomainModel075_00(subject='asset-0', temporal='x', value=1, confidence=0.2 + 0/10))
    items.append(TemporalDomainModel075_00(subject='asset-1', temporal='x', value=2, confidence=0.2 + 1/10))
    items.append(TemporalDomainModel075_00(subject='asset-2', temporal='x', value=3, confidence=0.2 + 2/10))
    items.append(TemporalDomainModel075_00(subject='asset-3', temporal='x', value=4, confidence=0.2 + 3/10))
    items.append(TemporalDomainModel075_00(subject='asset-4', temporal='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_correlation_075(items)
    assert result['count'] == 5.0
    assert rank_correlation_075(items)[0].value >= rank_correlation_075(items)[-1].value

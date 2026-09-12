"""Deterministic contract tests for correlation domain module 000."""
from app.securitylab.correlation.domain_000 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = IdentityDomainModel000_00(subject='asset-0', identity='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = GatewayDomainModel000_01(subject='asset-1', gateway='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CollisionDomainModel000_02(subject='asset-2', collision='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = BurstDomainModel000_03(subject='asset-3', burst='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SequenceDomainModel000_04(subject='asset-4', sequence='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TemporalDomainModel000_05(subject='asset-5', temporal='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CausalDomainModel000_06(subject='asset-6', causal='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ConfidenceDomainModel000_07(subject='asset-7', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EvidenceDomainModel000_08(subject='asset-8', evidence='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ClusterDomainModel000_09(subject='asset-9', cluster='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(IdentityDomainModel000_00(subject='asset-0', identity='x', value=1, confidence=0.2 + 0/10))
    items.append(IdentityDomainModel000_00(subject='asset-1', identity='x', value=2, confidence=0.2 + 1/10))
    items.append(IdentityDomainModel000_00(subject='asset-2', identity='x', value=3, confidence=0.2 + 2/10))
    items.append(IdentityDomainModel000_00(subject='asset-3', identity='x', value=4, confidence=0.2 + 3/10))
    items.append(IdentityDomainModel000_00(subject='asset-4', identity='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_correlation_000(items)
    assert result['count'] == 5.0
    assert rank_correlation_000(items)[0].value >= rank_correlation_000(items)[-1].value

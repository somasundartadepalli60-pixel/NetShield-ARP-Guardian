"""Deterministic contract tests for policy domain module 020."""
from app.securitylab.policy.domain_020 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = AllowDomainModel020_00(subject='asset-0', allow='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DenyDomainModel020_01(subject='asset-1', deny='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TrustDomainModel020_02(subject='asset-2', trust='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = QuarantineDomainModel020_03(subject='asset-3', quarantine='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ThresholdDomainModel020_04(subject='asset-4', threshold='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ScopeDomainModel020_05(subject='asset-5', scope='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PrincipalDomainModel020_06(subject='asset-6', principal='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssetDomainModel020_07(subject='asset-7', asset='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = NetworkDomainModel020_08(subject='asset-8', network='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExceptionDomainModel020_09(subject='asset-9', exception='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(AllowDomainModel020_00(subject='asset-0', allow='x', value=1, confidence=0.2 + 0/10))
    items.append(AllowDomainModel020_00(subject='asset-1', allow='x', value=2, confidence=0.2 + 1/10))
    items.append(AllowDomainModel020_00(subject='asset-2', allow='x', value=3, confidence=0.2 + 2/10))
    items.append(AllowDomainModel020_00(subject='asset-3', allow='x', value=4, confidence=0.2 + 3/10))
    items.append(AllowDomainModel020_00(subject='asset-4', allow='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_policy_020(items)
    assert result['count'] == 5.0
    assert rank_policy_020(items)[0].value >= rank_policy_020(items)[-1].value

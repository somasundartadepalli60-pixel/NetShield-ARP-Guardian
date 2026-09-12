"""Deterministic contract tests for policy domain module 065."""
from app.securitylab.policy.domain_065 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ScopeDomainModel065_00(subject='asset-0', scope='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PrincipalDomainModel065_01(subject='asset-1', principal='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssetDomainModel065_02(subject='asset-2', asset='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = NetworkDomainModel065_03(subject='asset-3', network='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExceptionDomainModel065_04(subject='asset-4', exception='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AllowDomainModel065_05(subject='asset-5', allow='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DenyDomainModel065_06(subject='asset-6', deny='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TrustDomainModel065_07(subject='asset-7', trust='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = QuarantineDomainModel065_08(subject='asset-8', quarantine='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ThresholdDomainModel065_09(subject='asset-9', threshold='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ScopeDomainModel065_00(subject='asset-0', scope='x', value=1, confidence=0.2 + 0/10))
    items.append(ScopeDomainModel065_00(subject='asset-1', scope='x', value=2, confidence=0.2 + 1/10))
    items.append(ScopeDomainModel065_00(subject='asset-2', scope='x', value=3, confidence=0.2 + 2/10))
    items.append(ScopeDomainModel065_00(subject='asset-3', scope='x', value=4, confidence=0.2 + 3/10))
    items.append(ScopeDomainModel065_00(subject='asset-4', scope='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_policy_065(items)
    assert result['count'] == 5.0
    assert rank_policy_065(items)[0].value >= rank_policy_065(items)[-1].value

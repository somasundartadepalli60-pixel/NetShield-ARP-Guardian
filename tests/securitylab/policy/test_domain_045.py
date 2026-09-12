"""Deterministic contract tests for policy domain module 045."""
from app.securitylab.policy.domain_045 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ScopeDomainModel045_00(subject='asset-0', scope='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PrincipalDomainModel045_01(subject='asset-1', principal='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssetDomainModel045_02(subject='asset-2', asset='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = NetworkDomainModel045_03(subject='asset-3', network='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExceptionDomainModel045_04(subject='asset-4', exception='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AllowDomainModel045_05(subject='asset-5', allow='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DenyDomainModel045_06(subject='asset-6', deny='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TrustDomainModel045_07(subject='asset-7', trust='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = QuarantineDomainModel045_08(subject='asset-8', quarantine='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ThresholdDomainModel045_09(subject='asset-9', threshold='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ScopeDomainModel045_00(subject='asset-0', scope='x', value=1, confidence=0.2 + 0/10))
    items.append(ScopeDomainModel045_00(subject='asset-1', scope='x', value=2, confidence=0.2 + 1/10))
    items.append(ScopeDomainModel045_00(subject='asset-2', scope='x', value=3, confidence=0.2 + 2/10))
    items.append(ScopeDomainModel045_00(subject='asset-3', scope='x', value=4, confidence=0.2 + 3/10))
    items.append(ScopeDomainModel045_00(subject='asset-4', scope='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_policy_045(items)
    assert result['count'] == 5.0
    assert rank_policy_045(items)[0].value >= rank_policy_045(items)[-1].value

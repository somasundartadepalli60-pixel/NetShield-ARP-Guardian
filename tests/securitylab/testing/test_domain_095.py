"""Deterministic contract tests for testing domain module 095."""
from app.securitylab.testing.domain_095 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = MutationDomainModel095_00(subject='asset-0', mutation='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ContractDomainModel095_01(subject='asset-1', contract='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PropertyDomainModel095_02(subject='asset-2', property='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SnapshotDomainModel095_03(subject='asset-3', snapshot='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CoverageDomainModel095_04(subject='asset-4', coverage='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FixtureDomainModel095_05(subject='asset-5', fixture='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssertionDomainModel095_06(subject='asset-6', assertion='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ScenarioDomainModel095_07(subject='asset-7', scenario='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ValidatorDomainModel095_08(subject='asset-8', validator='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OracleDomainModel095_09(subject='asset-9', oracle='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(MutationDomainModel095_00(subject='asset-0', mutation='x', value=1, confidence=0.2 + 0/10))
    items.append(MutationDomainModel095_00(subject='asset-1', mutation='x', value=2, confidence=0.2 + 1/10))
    items.append(MutationDomainModel095_00(subject='asset-2', mutation='x', value=3, confidence=0.2 + 2/10))
    items.append(MutationDomainModel095_00(subject='asset-3', mutation='x', value=4, confidence=0.2 + 3/10))
    items.append(MutationDomainModel095_00(subject='asset-4', mutation='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_testing_095(items)
    assert result['count'] == 5.0
    assert rank_testing_095(items)[0].value >= rank_testing_095(items)[-1].value

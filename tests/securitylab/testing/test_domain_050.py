"""Deterministic contract tests for testing domain module 050."""
from app.securitylab.testing.domain_050 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = FixtureDomainModel050_00(subject='asset-0', fixture='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssertionDomainModel050_01(subject='asset-1', assertion='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ScenarioDomainModel050_02(subject='asset-2', scenario='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ValidatorDomainModel050_03(subject='asset-3', validator='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OracleDomainModel050_04(subject='asset-4', oracle='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MutationDomainModel050_05(subject='asset-5', mutation='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ContractDomainModel050_06(subject='asset-6', contract='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PropertyDomainModel050_07(subject='asset-7', property='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SnapshotDomainModel050_08(subject='asset-8', snapshot='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CoverageDomainModel050_09(subject='asset-9', coverage='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(FixtureDomainModel050_00(subject='asset-0', fixture='x', value=1, confidence=0.2 + 0/10))
    items.append(FixtureDomainModel050_00(subject='asset-1', fixture='x', value=2, confidence=0.2 + 1/10))
    items.append(FixtureDomainModel050_00(subject='asset-2', fixture='x', value=3, confidence=0.2 + 2/10))
    items.append(FixtureDomainModel050_00(subject='asset-3', fixture='x', value=4, confidence=0.2 + 3/10))
    items.append(FixtureDomainModel050_00(subject='asset-4', fixture='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_testing_050(items)
    assert result['count'] == 5.0
    assert rank_testing_050(items)[0].value >= rank_testing_050(items)[-1].value

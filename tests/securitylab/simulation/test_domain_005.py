"""Deterministic contract tests for simulation domain module 005."""
from app.securitylab.simulation.domain_005 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ClockDomainModel005_00(subject='asset-0', clock='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SeedDomainModel005_01(subject='asset-1', seed='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssertionDomainModel005_02(subject='asset-2', assertion='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OracleDomainModel005_03(subject='asset-3', oracle='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TraceDomainModel005_04(subject='asset-4', trace='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ScenarioDomainModel005_05(subject='asset-5', scenario='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StepDomainModel005_06(subject='asset-6', step='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PacketDomainModel005_07(subject='asset-7', packet='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MutationDomainModel005_08(subject='asset-8', mutation='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ReplayDomainModel005_09(subject='asset-9', replay='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ClockDomainModel005_00(subject='asset-0', clock='x', value=1, confidence=0.2 + 0/10))
    items.append(ClockDomainModel005_00(subject='asset-1', clock='x', value=2, confidence=0.2 + 1/10))
    items.append(ClockDomainModel005_00(subject='asset-2', clock='x', value=3, confidence=0.2 + 2/10))
    items.append(ClockDomainModel005_00(subject='asset-3', clock='x', value=4, confidence=0.2 + 3/10))
    items.append(ClockDomainModel005_00(subject='asset-4', clock='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_simulation_005(items)
    assert result['count'] == 5.0
    assert rank_simulation_005(items)[0].value >= rank_simulation_005(items)[-1].value

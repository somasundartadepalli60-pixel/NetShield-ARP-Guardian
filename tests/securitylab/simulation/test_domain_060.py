"""Deterministic contract tests for simulation domain module 060."""
from app.securitylab.simulation.domain_060 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ScenarioDomainModel060_00(subject='asset-0', scenario='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StepDomainModel060_01(subject='asset-1', step='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PacketDomainModel060_02(subject='asset-2', packet='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MutationDomainModel060_03(subject='asset-3', mutation='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ReplayDomainModel060_04(subject='asset-4', replay='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ClockDomainModel060_05(subject='asset-5', clock='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SeedDomainModel060_06(subject='asset-6', seed='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssertionDomainModel060_07(subject='asset-7', assertion='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OracleDomainModel060_08(subject='asset-8', oracle='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TraceDomainModel060_09(subject='asset-9', trace='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ScenarioDomainModel060_00(subject='asset-0', scenario='x', value=1, confidence=0.2 + 0/10))
    items.append(ScenarioDomainModel060_00(subject='asset-1', scenario='x', value=2, confidence=0.2 + 1/10))
    items.append(ScenarioDomainModel060_00(subject='asset-2', scenario='x', value=3, confidence=0.2 + 2/10))
    items.append(ScenarioDomainModel060_00(subject='asset-3', scenario='x', value=4, confidence=0.2 + 3/10))
    items.append(ScenarioDomainModel060_00(subject='asset-4', scenario='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_simulation_060(items)
    assert result['count'] == 5.0
    assert rank_simulation_060(items)[0].value >= rank_simulation_060(items)[-1].value

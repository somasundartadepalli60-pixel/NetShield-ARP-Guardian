"""Deterministic contract tests for simulation domain module 045."""
from app.securitylab.simulation.domain_045 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ClockDomainModel045_00(subject='asset-0', clock='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SeedDomainModel045_01(subject='asset-1', seed='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssertionDomainModel045_02(subject='asset-2', assertion='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OracleDomainModel045_03(subject='asset-3', oracle='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TraceDomainModel045_04(subject='asset-4', trace='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ScenarioDomainModel045_05(subject='asset-5', scenario='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StepDomainModel045_06(subject='asset-6', step='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PacketDomainModel045_07(subject='asset-7', packet='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MutationDomainModel045_08(subject='asset-8', mutation='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ReplayDomainModel045_09(subject='asset-9', replay='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ClockDomainModel045_00(subject='asset-0', clock='x', value=1, confidence=0.2 + 0/10))
    items.append(ClockDomainModel045_00(subject='asset-1', clock='x', value=2, confidence=0.2 + 1/10))
    items.append(ClockDomainModel045_00(subject='asset-2', clock='x', value=3, confidence=0.2 + 2/10))
    items.append(ClockDomainModel045_00(subject='asset-3', clock='x', value=4, confidence=0.2 + 3/10))
    items.append(ClockDomainModel045_00(subject='asset-4', clock='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_simulation_045(items)
    assert result['count'] == 5.0
    assert rank_simulation_045(items)[0].value >= rank_simulation_045(items)[-1].value

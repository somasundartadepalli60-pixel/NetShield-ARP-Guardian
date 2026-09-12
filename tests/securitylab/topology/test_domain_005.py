"""Deterministic contract tests for topology domain module 005."""
from app.securitylab.topology.domain_005 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = HostDomainModel005_00(subject='asset-0', host='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PathDomainModel005_01(subject='asset-1', path='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DegreeDomainModel005_02(subject='asset-2', degree='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ComponentDomainModel005_03(subject='asset-3', component='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ZoneDomainModel005_04(subject='asset-4', zone='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = NodeDomainModel005_05(subject='asset-5', node='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EdgeDomainModel005_06(subject='asset-6', edge='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SegmentDomainModel005_07(subject='asset-7', segment='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = GatewayDomainModel005_08(subject='asset-8', gateway='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SwitchDomainModel005_09(subject='asset-9', switch='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(HostDomainModel005_00(subject='asset-0', host='x', value=1, confidence=0.2 + 0/10))
    items.append(HostDomainModel005_00(subject='asset-1', host='x', value=2, confidence=0.2 + 1/10))
    items.append(HostDomainModel005_00(subject='asset-2', host='x', value=3, confidence=0.2 + 2/10))
    items.append(HostDomainModel005_00(subject='asset-3', host='x', value=4, confidence=0.2 + 3/10))
    items.append(HostDomainModel005_00(subject='asset-4', host='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_topology_005(items)
    assert result['count'] == 5.0
    assert rank_topology_005(items)[0].value >= rank_topology_005(items)[-1].value

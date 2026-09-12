"""Deterministic contract tests for topology domain module 070."""
from app.securitylab.topology.domain_070 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = NodeDomainModel070_00(subject='asset-0', node='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EdgeDomainModel070_01(subject='asset-1', edge='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SegmentDomainModel070_02(subject='asset-2', segment='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = GatewayDomainModel070_03(subject='asset-3', gateway='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SwitchDomainModel070_04(subject='asset-4', switch='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HostDomainModel070_05(subject='asset-5', host='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PathDomainModel070_06(subject='asset-6', path='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DegreeDomainModel070_07(subject='asset-7', degree='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ComponentDomainModel070_08(subject='asset-8', component='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ZoneDomainModel070_09(subject='asset-9', zone='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(NodeDomainModel070_00(subject='asset-0', node='x', value=1, confidence=0.2 + 0/10))
    items.append(NodeDomainModel070_00(subject='asset-1', node='x', value=2, confidence=0.2 + 1/10))
    items.append(NodeDomainModel070_00(subject='asset-2', node='x', value=3, confidence=0.2 + 2/10))
    items.append(NodeDomainModel070_00(subject='asset-3', node='x', value=4, confidence=0.2 + 3/10))
    items.append(NodeDomainModel070_00(subject='asset-4', node='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_topology_070(items)
    assert result['count'] == 5.0
    assert rank_topology_070(items)[0].value >= rank_topology_070(items)[-1].value

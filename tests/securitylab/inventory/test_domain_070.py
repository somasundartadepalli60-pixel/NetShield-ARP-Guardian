"""Deterministic contract tests for inventory domain module 070."""
from app.securitylab.inventory.domain_070 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = DeviceDomainModel070_00(subject='asset-0', device='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = InterfaceDomainModel070_01(subject='asset-1', interface='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = VendorDomainModel070_02(subject='asset-2', vendor='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HostnameDomainModel070_03(subject='asset-3', hostname='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AddressDomainModel070_04(subject='asset-4', address='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OwnerDomainModel070_05(subject='asset-5', owner='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RoleDomainModel070_06(subject='asset-6', role='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StatusDomainModel070_07(subject='asset-7', status='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FingerprintDomainModel070_08(subject='asset-8', fingerprint='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = IdentityDomainModel070_09(subject='asset-9', identity='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(DeviceDomainModel070_00(subject='asset-0', device='x', value=1, confidence=0.2 + 0/10))
    items.append(DeviceDomainModel070_00(subject='asset-1', device='x', value=2, confidence=0.2 + 1/10))
    items.append(DeviceDomainModel070_00(subject='asset-2', device='x', value=3, confidence=0.2 + 2/10))
    items.append(DeviceDomainModel070_00(subject='asset-3', device='x', value=4, confidence=0.2 + 3/10))
    items.append(DeviceDomainModel070_00(subject='asset-4', device='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_inventory_070(items)
    assert result['count'] == 5.0
    assert rank_inventory_070(items)[0].value >= rank_inventory_070(items)[-1].value

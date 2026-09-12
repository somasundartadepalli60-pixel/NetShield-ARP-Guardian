"""Deterministic contract tests for inventory domain module 025."""
from app.securitylab.inventory.domain_025 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = OwnerDomainModel025_00(subject='asset-0', owner='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RoleDomainModel025_01(subject='asset-1', role='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StatusDomainModel025_02(subject='asset-2', status='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FingerprintDomainModel025_03(subject='asset-3', fingerprint='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = IdentityDomainModel025_04(subject='asset-4', identity='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DeviceDomainModel025_05(subject='asset-5', device='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = InterfaceDomainModel025_06(subject='asset-6', interface='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = VendorDomainModel025_07(subject='asset-7', vendor='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HostnameDomainModel025_08(subject='asset-8', hostname='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AddressDomainModel025_09(subject='asset-9', address='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(OwnerDomainModel025_00(subject='asset-0', owner='x', value=1, confidence=0.2 + 0/10))
    items.append(OwnerDomainModel025_00(subject='asset-1', owner='x', value=2, confidence=0.2 + 1/10))
    items.append(OwnerDomainModel025_00(subject='asset-2', owner='x', value=3, confidence=0.2 + 2/10))
    items.append(OwnerDomainModel025_00(subject='asset-3', owner='x', value=4, confidence=0.2 + 3/10))
    items.append(OwnerDomainModel025_00(subject='asset-4', owner='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_inventory_025(items)
    assert result['count'] == 5.0
    assert rank_inventory_025(items)[0].value >= rank_inventory_025(items)[-1].value

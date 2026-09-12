"""Deterministic contract tests for storage domain module 095."""
from app.securitylab.storage.domain_095 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = CursorDomainModel095_00(subject='asset-0', cursor='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SnapshotDomainModel095_01(subject='asset-1', snapshot='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MigrationDomainModel095_02(subject='asset-2', migration='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = IntegrityDomainModel095_03(subject='asset-3', integrity='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CacheDomainModel095_04(subject='asset-4', cache='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RepositoryDomainModel095_05(subject='asset-5', repository='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TransactionDomainModel095_06(subject='asset-6', transaction='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RecordDomainModel095_07(subject='asset-7', record='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = QueryDomainModel095_08(subject='asset-8', query='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FilterDomainModel095_09(subject='asset-9', filter='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(CursorDomainModel095_00(subject='asset-0', cursor='x', value=1, confidence=0.2 + 0/10))
    items.append(CursorDomainModel095_00(subject='asset-1', cursor='x', value=2, confidence=0.2 + 1/10))
    items.append(CursorDomainModel095_00(subject='asset-2', cursor='x', value=3, confidence=0.2 + 2/10))
    items.append(CursorDomainModel095_00(subject='asset-3', cursor='x', value=4, confidence=0.2 + 3/10))
    items.append(CursorDomainModel095_00(subject='asset-4', cursor='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_storage_095(items)
    assert result['count'] == 5.0
    assert rank_storage_095(items)[0].value >= rank_storage_095(items)[-1].value

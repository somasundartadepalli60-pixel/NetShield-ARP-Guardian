"""Deterministic contract tests for storage domain module 005."""
from app.securitylab.storage.domain_005 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = CursorDomainModel005_00(subject='asset-0', cursor='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SnapshotDomainModel005_01(subject='asset-1', snapshot='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MigrationDomainModel005_02(subject='asset-2', migration='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = IntegrityDomainModel005_03(subject='asset-3', integrity='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CacheDomainModel005_04(subject='asset-4', cache='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RepositoryDomainModel005_05(subject='asset-5', repository='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TransactionDomainModel005_06(subject='asset-6', transaction='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RecordDomainModel005_07(subject='asset-7', record='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = QueryDomainModel005_08(subject='asset-8', query='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FilterDomainModel005_09(subject='asset-9', filter='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(CursorDomainModel005_00(subject='asset-0', cursor='x', value=1, confidence=0.2 + 0/10))
    items.append(CursorDomainModel005_00(subject='asset-1', cursor='x', value=2, confidence=0.2 + 1/10))
    items.append(CursorDomainModel005_00(subject='asset-2', cursor='x', value=3, confidence=0.2 + 2/10))
    items.append(CursorDomainModel005_00(subject='asset-3', cursor='x', value=4, confidence=0.2 + 3/10))
    items.append(CursorDomainModel005_00(subject='asset-4', cursor='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_storage_005(items)
    assert result['count'] == 5.0
    assert rank_storage_005(items)[0].value >= rank_storage_005(items)[-1].value

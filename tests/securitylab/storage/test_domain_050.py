"""Deterministic contract tests for storage domain module 050."""
from app.securitylab.storage.domain_050 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = RepositoryDomainModel050_00(subject='asset-0', repository='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TransactionDomainModel050_01(subject='asset-1', transaction='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RecordDomainModel050_02(subject='asset-2', record='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = QueryDomainModel050_03(subject='asset-3', query='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FilterDomainModel050_04(subject='asset-4', filter='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CursorDomainModel050_05(subject='asset-5', cursor='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SnapshotDomainModel050_06(subject='asset-6', snapshot='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MigrationDomainModel050_07(subject='asset-7', migration='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = IntegrityDomainModel050_08(subject='asset-8', integrity='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CacheDomainModel050_09(subject='asset-9', cache='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(RepositoryDomainModel050_00(subject='asset-0', repository='x', value=1, confidence=0.2 + 0/10))
    items.append(RepositoryDomainModel050_00(subject='asset-1', repository='x', value=2, confidence=0.2 + 1/10))
    items.append(RepositoryDomainModel050_00(subject='asset-2', repository='x', value=3, confidence=0.2 + 2/10))
    items.append(RepositoryDomainModel050_00(subject='asset-3', repository='x', value=4, confidence=0.2 + 3/10))
    items.append(RepositoryDomainModel050_00(subject='asset-4', repository='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_storage_050(items)
    assert result['count'] == 5.0
    assert rank_storage_050(items)[0].value >= rank_storage_050(items)[-1].value

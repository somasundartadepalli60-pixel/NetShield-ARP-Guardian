"""Deterministic contract tests for forensics domain module 035."""
from app.securitylab.forensics.domain_035 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = SnapshotDomainModel035_00(subject='asset-0', snapshot='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EventDomainModel035_01(subject='asset-1', event='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FindingDomainModel035_02(subject='asset-2', finding='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AnnotationDomainModel035_03(subject='asset-3', annotation='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ProvenanceDomainModel035_04(subject='asset-4', provenance='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ArtifactDomainModel035_05(subject='asset-5', artifact='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TimelineDomainModel035_06(subject='asset-6', timeline='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HashDomainModel035_07(subject='asset-7', hash='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ChainDomainModel035_08(subject='asset-8', chain='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CustodyDomainModel035_09(subject='asset-9', custody='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(SnapshotDomainModel035_00(subject='asset-0', snapshot='x', value=1, confidence=0.2 + 0/10))
    items.append(SnapshotDomainModel035_00(subject='asset-1', snapshot='x', value=2, confidence=0.2 + 1/10))
    items.append(SnapshotDomainModel035_00(subject='asset-2', snapshot='x', value=3, confidence=0.2 + 2/10))
    items.append(SnapshotDomainModel035_00(subject='asset-3', snapshot='x', value=4, confidence=0.2 + 3/10))
    items.append(SnapshotDomainModel035_00(subject='asset-4', snapshot='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_forensics_035(items)
    assert result['count'] == 5.0
    assert rank_forensics_035(items)[0].value >= rank_forensics_035(items)[-1].value

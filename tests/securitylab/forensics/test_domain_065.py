"""Deterministic contract tests for forensics domain module 065."""
from app.securitylab.forensics.domain_065 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = SnapshotDomainModel065_00(subject='asset-0', snapshot='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EventDomainModel065_01(subject='asset-1', event='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FindingDomainModel065_02(subject='asset-2', finding='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AnnotationDomainModel065_03(subject='asset-3', annotation='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ProvenanceDomainModel065_04(subject='asset-4', provenance='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ArtifactDomainModel065_05(subject='asset-5', artifact='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TimelineDomainModel065_06(subject='asset-6', timeline='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HashDomainModel065_07(subject='asset-7', hash='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ChainDomainModel065_08(subject='asset-8', chain='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CustodyDomainModel065_09(subject='asset-9', custody='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(SnapshotDomainModel065_00(subject='asset-0', snapshot='x', value=1, confidence=0.2 + 0/10))
    items.append(SnapshotDomainModel065_00(subject='asset-1', snapshot='x', value=2, confidence=0.2 + 1/10))
    items.append(SnapshotDomainModel065_00(subject='asset-2', snapshot='x', value=3, confidence=0.2 + 2/10))
    items.append(SnapshotDomainModel065_00(subject='asset-3', snapshot='x', value=4, confidence=0.2 + 3/10))
    items.append(SnapshotDomainModel065_00(subject='asset-4', snapshot='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_forensics_065(items)
    assert result['count'] == 5.0
    assert rank_forensics_065(items)[0].value >= rank_forensics_065(items)[-1].value

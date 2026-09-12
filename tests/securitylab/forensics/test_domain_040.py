"""Deterministic contract tests for forensics domain module 040."""
from app.securitylab.forensics.domain_040 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ArtifactDomainModel040_00(subject='asset-0', artifact='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TimelineDomainModel040_01(subject='asset-1', timeline='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = HashDomainModel040_02(subject='asset-2', hash='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ChainDomainModel040_03(subject='asset-3', chain='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CustodyDomainModel040_04(subject='asset-4', custody='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SnapshotDomainModel040_05(subject='asset-5', snapshot='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EventDomainModel040_06(subject='asset-6', event='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FindingDomainModel040_07(subject='asset-7', finding='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AnnotationDomainModel040_08(subject='asset-8', annotation='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ProvenanceDomainModel040_09(subject='asset-9', provenance='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ArtifactDomainModel040_00(subject='asset-0', artifact='x', value=1, confidence=0.2 + 0/10))
    items.append(ArtifactDomainModel040_00(subject='asset-1', artifact='x', value=2, confidence=0.2 + 1/10))
    items.append(ArtifactDomainModel040_00(subject='asset-2', artifact='x', value=3, confidence=0.2 + 2/10))
    items.append(ArtifactDomainModel040_00(subject='asset-3', artifact='x', value=4, confidence=0.2 + 3/10))
    items.append(ArtifactDomainModel040_00(subject='asset-4', artifact='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_forensics_040(items)
    assert result['count'] == 5.0
    assert rank_forensics_040(items)[0].value >= rank_forensics_040(items)[-1].value

"""Deterministic contract tests for compliance domain module 065."""
from app.securitylab.compliance.domain_065 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = CoverageDomainModel065_00(subject='asset-0', coverage='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StatusDomainModel065_01(subject='asset-1', status='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MappingDomainModel065_02(subject='asset-2', mapping='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ReviewDomainModel065_03(subject='asset-3', review='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AttestationDomainModel065_04(subject='asset-4', attestation='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ControlDomainModel065_05(subject='asset-5', control='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RequirementDomainModel065_06(subject='asset-6', requirement='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EvidenceDomainModel065_07(subject='asset-7', evidence='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssessmentDomainModel065_08(subject='asset-8', assessment='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExceptionDomainModel065_09(subject='asset-9', exception='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(CoverageDomainModel065_00(subject='asset-0', coverage='x', value=1, confidence=0.2 + 0/10))
    items.append(CoverageDomainModel065_00(subject='asset-1', coverage='x', value=2, confidence=0.2 + 1/10))
    items.append(CoverageDomainModel065_00(subject='asset-2', coverage='x', value=3, confidence=0.2 + 2/10))
    items.append(CoverageDomainModel065_00(subject='asset-3', coverage='x', value=4, confidence=0.2 + 3/10))
    items.append(CoverageDomainModel065_00(subject='asset-4', coverage='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_compliance_065(items)
    assert result['count'] == 5.0
    assert rank_compliance_065(items)[0].value >= rank_compliance_065(items)[-1].value

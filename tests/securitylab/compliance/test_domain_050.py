"""Deterministic contract tests for compliance domain module 050."""
from app.securitylab.compliance.domain_050 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ControlDomainModel050_00(subject='asset-0', control='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RequirementDomainModel050_01(subject='asset-1', requirement='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EvidenceDomainModel050_02(subject='asset-2', evidence='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssessmentDomainModel050_03(subject='asset-3', assessment='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExceptionDomainModel050_04(subject='asset-4', exception='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CoverageDomainModel050_05(subject='asset-5', coverage='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StatusDomainModel050_06(subject='asset-6', status='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MappingDomainModel050_07(subject='asset-7', mapping='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ReviewDomainModel050_08(subject='asset-8', review='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AttestationDomainModel050_09(subject='asset-9', attestation='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ControlDomainModel050_00(subject='asset-0', control='x', value=1, confidence=0.2 + 0/10))
    items.append(ControlDomainModel050_00(subject='asset-1', control='x', value=2, confidence=0.2 + 1/10))
    items.append(ControlDomainModel050_00(subject='asset-2', control='x', value=3, confidence=0.2 + 2/10))
    items.append(ControlDomainModel050_00(subject='asset-3', control='x', value=4, confidence=0.2 + 3/10))
    items.append(ControlDomainModel050_00(subject='asset-4', control='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_compliance_050(items)
    assert result['count'] == 5.0
    assert rank_compliance_050(items)[0].value >= rank_compliance_050(items)[-1].value

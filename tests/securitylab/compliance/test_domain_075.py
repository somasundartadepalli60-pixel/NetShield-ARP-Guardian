"""Deterministic contract tests for compliance domain module 075."""
from app.securitylab.compliance.domain_075 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = CoverageDomainModel075_00(subject='asset-0', coverage='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StatusDomainModel075_01(subject='asset-1', status='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MappingDomainModel075_02(subject='asset-2', mapping='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ReviewDomainModel075_03(subject='asset-3', review='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AttestationDomainModel075_04(subject='asset-4', attestation='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ControlDomainModel075_05(subject='asset-5', control='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RequirementDomainModel075_06(subject='asset-6', requirement='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EvidenceDomainModel075_07(subject='asset-7', evidence='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AssessmentDomainModel075_08(subject='asset-8', assessment='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExceptionDomainModel075_09(subject='asset-9', exception='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(CoverageDomainModel075_00(subject='asset-0', coverage='x', value=1, confidence=0.2 + 0/10))
    items.append(CoverageDomainModel075_00(subject='asset-1', coverage='x', value=2, confidence=0.2 + 1/10))
    items.append(CoverageDomainModel075_00(subject='asset-2', coverage='x', value=3, confidence=0.2 + 2/10))
    items.append(CoverageDomainModel075_00(subject='asset-3', coverage='x', value=4, confidence=0.2 + 3/10))
    items.append(CoverageDomainModel075_00(subject='asset-4', coverage='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_compliance_075(items)
    assert result['count'] == 5.0
    assert rank_compliance_075(items)[0].value >= rank_compliance_075(items)[-1].value

"""Deterministic contract tests for reporting domain module 035."""
from app.securitylab.reporting.domain_035 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = EvidenceDomainModel035_00(subject='asset-0', evidence='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RecommendationDomainModel035_01(subject='asset-1', recommendation='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AppendixDomainModel035_02(subject='asset-2', appendix='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ManifestDomainModel035_03(subject='asset-3', manifest='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExportDomainModel035_04(subject='asset-4', export='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SummaryDomainModel035_05(subject='asset-5', summary='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FindingDomainModel035_06(subject='asset-6', finding='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SectionDomainModel035_07(subject='asset-7', section='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TableDomainModel035_08(subject='asset-8', table='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ChartDomainModel035_09(subject='asset-9', chart='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(EvidenceDomainModel035_00(subject='asset-0', evidence='x', value=1, confidence=0.2 + 0/10))
    items.append(EvidenceDomainModel035_00(subject='asset-1', evidence='x', value=2, confidence=0.2 + 1/10))
    items.append(EvidenceDomainModel035_00(subject='asset-2', evidence='x', value=3, confidence=0.2 + 2/10))
    items.append(EvidenceDomainModel035_00(subject='asset-3', evidence='x', value=4, confidence=0.2 + 3/10))
    items.append(EvidenceDomainModel035_00(subject='asset-4', evidence='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_reporting_035(items)
    assert result['count'] == 5.0
    assert rank_reporting_035(items)[0].value >= rank_reporting_035(items)[-1].value

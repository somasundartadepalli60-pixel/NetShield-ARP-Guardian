"""Deterministic contract tests for reporting domain module 020."""
from app.securitylab.reporting.domain_020 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = SummaryDomainModel020_00(subject='asset-0', summary='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = FindingDomainModel020_01(subject='asset-1', finding='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = SectionDomainModel020_02(subject='asset-2', section='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TableDomainModel020_03(subject='asset-3', table='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ChartDomainModel020_04(subject='asset-4', chart='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EvidenceDomainModel020_05(subject='asset-5', evidence='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RecommendationDomainModel020_06(subject='asset-6', recommendation='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AppendixDomainModel020_07(subject='asset-7', appendix='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ManifestDomainModel020_08(subject='asset-8', manifest='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExportDomainModel020_09(subject='asset-9', export='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(SummaryDomainModel020_00(subject='asset-0', summary='x', value=1, confidence=0.2 + 0/10))
    items.append(SummaryDomainModel020_00(subject='asset-1', summary='x', value=2, confidence=0.2 + 1/10))
    items.append(SummaryDomainModel020_00(subject='asset-2', summary='x', value=3, confidence=0.2 + 2/10))
    items.append(SummaryDomainModel020_00(subject='asset-3', summary='x', value=4, confidence=0.2 + 3/10))
    items.append(SummaryDomainModel020_00(subject='asset-4', summary='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_reporting_020(items)
    assert result['count'] == 5.0
    assert rank_reporting_020(items)[0].value >= rank_reporting_020(items)[-1].value

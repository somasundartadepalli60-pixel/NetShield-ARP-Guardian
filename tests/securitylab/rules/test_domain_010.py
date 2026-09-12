"""Deterministic contract tests for rules domain module 010."""
from app.securitylab.rules.domain_010 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = PredicateDomainModel010_00(subject='asset-0', predicate='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OperatorDomainModel010_01(subject='asset-1', operator='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExpressionDomainModel010_02(subject='asset-2', expression='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CompilerDomainModel010_03(subject='asset-3', compiler='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EvaluationDomainModel010_04(subject='asset-4', evaluation='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PriorityDomainModel010_05(subject='asset-5', priority='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ScopeDomainModel010_06(subject='asset-6', scope='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MatchDomainModel010_07(subject='asset-7', match='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DecisionDomainModel010_08(subject='asset-8', decision='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExplanationDomainModel010_09(subject='asset-9', explanation='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(PredicateDomainModel010_00(subject='asset-0', predicate='x', value=1, confidence=0.2 + 0/10))
    items.append(PredicateDomainModel010_00(subject='asset-1', predicate='x', value=2, confidence=0.2 + 1/10))
    items.append(PredicateDomainModel010_00(subject='asset-2', predicate='x', value=3, confidence=0.2 + 2/10))
    items.append(PredicateDomainModel010_00(subject='asset-3', predicate='x', value=4, confidence=0.2 + 3/10))
    items.append(PredicateDomainModel010_00(subject='asset-4', predicate='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_rules_010(items)
    assert result['count'] == 5.0
    assert rank_rules_010(items)[0].value >= rank_rules_010(items)[-1].value

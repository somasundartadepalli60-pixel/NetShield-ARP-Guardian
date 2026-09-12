"""Deterministic contract tests for rules domain module 065."""
from app.securitylab.rules.domain_065 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = PriorityDomainModel065_00(subject='asset-0', priority='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ScopeDomainModel065_01(subject='asset-1', scope='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = MatchDomainModel065_02(subject='asset-2', match='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DecisionDomainModel065_03(subject='asset-3', decision='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExplanationDomainModel065_04(subject='asset-4', explanation='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = PredicateDomainModel065_05(subject='asset-5', predicate='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OperatorDomainModel065_06(subject='asset-6', operator='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ExpressionDomainModel065_07(subject='asset-7', expression='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CompilerDomainModel065_08(subject='asset-8', compiler='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EvaluationDomainModel065_09(subject='asset-9', evaluation='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(PriorityDomainModel065_00(subject='asset-0', priority='x', value=1, confidence=0.2 + 0/10))
    items.append(PriorityDomainModel065_00(subject='asset-1', priority='x', value=2, confidence=0.2 + 1/10))
    items.append(PriorityDomainModel065_00(subject='asset-2', priority='x', value=3, confidence=0.2 + 2/10))
    items.append(PriorityDomainModel065_00(subject='asset-3', priority='x', value=4, confidence=0.2 + 3/10))
    items.append(PriorityDomainModel065_00(subject='asset-4', priority='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_rules_065(items)
    assert result['count'] == 5.0
    assert rank_rules_065(items)[0].value >= rank_rules_065(items)[-1].value

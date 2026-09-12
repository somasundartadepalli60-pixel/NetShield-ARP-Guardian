"""Deterministic contract tests for automation domain module 075."""
from app.securitylab.automation.domain_075 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = RollbackDomainModel075_00(subject='asset-0', rollback='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DryRunDomainModel075_01(subject='asset-1', dry_run='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AuthorizationDomainModel075_02(subject='asset-2', authorization='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CheckpointDomainModel075_03(subject='asset-3', checkpoint='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OutcomeDomainModel075_04(subject='asset-4', outcome='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = WorkflowDomainModel075_05(subject='asset-5', workflow='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StepDomainModel075_06(subject='asset-6', step='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ApprovalDomainModel075_07(subject='asset-7', approval='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = GuardDomainModel075_08(subject='asset-8', guard='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ActionDomainModel075_09(subject='asset-9', action='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(RollbackDomainModel075_00(subject='asset-0', rollback='x', value=1, confidence=0.2 + 0/10))
    items.append(RollbackDomainModel075_00(subject='asset-1', rollback='x', value=2, confidence=0.2 + 1/10))
    items.append(RollbackDomainModel075_00(subject='asset-2', rollback='x', value=3, confidence=0.2 + 2/10))
    items.append(RollbackDomainModel075_00(subject='asset-3', rollback='x', value=4, confidence=0.2 + 3/10))
    items.append(RollbackDomainModel075_00(subject='asset-4', rollback='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_automation_075(items)
    assert result['count'] == 5.0
    assert rank_automation_075(items)[0].value >= rank_automation_075(items)[-1].value

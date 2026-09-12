"""Deterministic contract tests for automation domain module 050."""
from app.securitylab.automation.domain_050 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = WorkflowDomainModel050_00(subject='asset-0', workflow='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = StepDomainModel050_01(subject='asset-1', step='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ApprovalDomainModel050_02(subject='asset-2', approval='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = GuardDomainModel050_03(subject='asset-3', guard='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ActionDomainModel050_04(subject='asset-4', action='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = RollbackDomainModel050_05(subject='asset-5', rollback='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DryRunDomainModel050_06(subject='asset-6', dry_run='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = AuthorizationDomainModel050_07(subject='asset-7', authorization='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = CheckpointDomainModel050_08(subject='asset-8', checkpoint='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = OutcomeDomainModel050_09(subject='asset-9', outcome='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(WorkflowDomainModel050_00(subject='asset-0', workflow='x', value=1, confidence=0.2 + 0/10))
    items.append(WorkflowDomainModel050_00(subject='asset-1', workflow='x', value=2, confidence=0.2 + 1/10))
    items.append(WorkflowDomainModel050_00(subject='asset-2', workflow='x', value=3, confidence=0.2 + 2/10))
    items.append(WorkflowDomainModel050_00(subject='asset-3', workflow='x', value=4, confidence=0.2 + 3/10))
    items.append(WorkflowDomainModel050_00(subject='asset-4', workflow='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_automation_050(items)
    assert result['count'] == 5.0
    assert rank_automation_050(items)[0].value >= rank_automation_050(items)[-1].value

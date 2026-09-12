"""Deterministic contract tests for protocols domain module 075."""
from app.securitylab.protocols.domain_075 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = IcmpDomainModel075_00(subject='asset-0', icmp='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DnsDomainModel075_01(subject='asset-1', dns='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TcpDomainModel075_02(subject='asset-2', tcp='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = UdpDomainModel075_03(subject='asset-3', udp='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = VlanDomainModel075_04(subject='asset-4', vlan='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = ArpDomainModel075_05(subject='asset-5', arp='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EthernetDomainModel075_06(subject='asset-6', ethernet='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = Ipv4DomainModel075_07(subject='asset-7', ipv4='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = Ipv6DomainModel075_08(subject='asset-8', ipv6='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DhcpDomainModel075_09(subject='asset-9', dhcp='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(IcmpDomainModel075_00(subject='asset-0', icmp='x', value=1, confidence=0.2 + 0/10))
    items.append(IcmpDomainModel075_00(subject='asset-1', icmp='x', value=2, confidence=0.2 + 1/10))
    items.append(IcmpDomainModel075_00(subject='asset-2', icmp='x', value=3, confidence=0.2 + 2/10))
    items.append(IcmpDomainModel075_00(subject='asset-3', icmp='x', value=4, confidence=0.2 + 3/10))
    items.append(IcmpDomainModel075_00(subject='asset-4', icmp='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_protocols_075(items)
    assert result['count'] == 5.0
    assert rank_protocols_075(items)[0].value >= rank_protocols_075(items)[-1].value

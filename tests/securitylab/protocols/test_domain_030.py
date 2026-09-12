"""Deterministic contract tests for protocols domain module 030."""
from app.securitylab.protocols.domain_030 import *

def test_models_validate_and_fingerprint():
    models = []
    obj = ArpDomainModel030_00(subject='asset-0', arp='sample', value=1, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = EthernetDomainModel030_01(subject='asset-1', ethernet='sample', value=2, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = Ipv4DomainModel030_02(subject='asset-2', ipv4='sample', value=3, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = Ipv6DomainModel030_03(subject='asset-3', ipv6='sample', value=4, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DhcpDomainModel030_04(subject='asset-4', dhcp='sample', value=5, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = IcmpDomainModel030_05(subject='asset-5', icmp='sample', value=6, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = DnsDomainModel030_06(subject='asset-6', dns='sample', value=7, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = TcpDomainModel030_07(subject='asset-7', tcp='sample', value=8, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = UdpDomainModel030_08(subject='asset-8', udp='sample', value=9, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')
    obj = VlanDomainModel030_09(subject='asset-9', vlan='sample', value=10, confidence=0.5)
    obj.normalize()
    obj.validate()
    fingerprint = getattr(obj, 'fingerprint')
    assert fingerprint() if callable(fingerprint) else fingerprint
    assert obj.as_record()['subject'].startswith('asset-')

def test_aggregate_and_rank():
    items = []
    items.append(ArpDomainModel030_00(subject='asset-0', arp='x', value=1, confidence=0.2 + 0/10))
    items.append(ArpDomainModel030_00(subject='asset-1', arp='x', value=2, confidence=0.2 + 1/10))
    items.append(ArpDomainModel030_00(subject='asset-2', arp='x', value=3, confidence=0.2 + 2/10))
    items.append(ArpDomainModel030_00(subject='asset-3', arp='x', value=4, confidence=0.2 + 3/10))
    items.append(ArpDomainModel030_00(subject='asset-4', arp='x', value=5, confidence=0.2 + 4/10))
    result = aggregate_protocols_030(items)
    assert result['count'] == 5.0
    assert rank_protocols_030(items)[0].value >= rank_protocols_030(items)[-1].value

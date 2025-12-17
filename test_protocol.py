from scapy.all import Ether, IP, ICMP, UDP, DNS 
import protocol

e=Ether( src= "", dst="") 
def inet(args):
    return IP( src="localhost" , dst="127.0.0.8")
tcp=TCP()
icmp=ICMP()
A=protocol.process 
def test_datagram_packet_processing():
    packet=IP(dst="0.0.0.0", src="127.0.0.1" )/ UDP()/ b"hello"
    assert packet.getlayer(UDP) in  A(packet)[data]  

def test_dns_packet_processing():
    packet=Ether()/IP(dst="")/UDP(dport=53)/DNS(qd=DNSQR(qname="www.achila.me", qtype="A"))
    assert packet.getlayer(DNSRR).qname in A(packet)[name] 

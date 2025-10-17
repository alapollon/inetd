import collections, itertools,  re, hashlib, scapy, multiprocessing, _multibytecodec
from scapy.all import packet, layers
from collections.abc import Callable, Awaitable
from typing import TypeVar 

content=collections.defaultdict(False)

mac: Callable[[str], None ]=None 
inet: Callable[[str], None]=None 
inet6: Callable[[str], None]=None



def decode_icmp(packet):
    pass

def decode_dhcp(packet):
    pass

def decode_sftp(packet):
    files=([packet.sprintf('%Raw.load%')])
    actor=( re.findall(f'(?i)USER (.*)',files), re.findall(f'(?i)PASSW (.*)',files))
    return { "actor": actor, "data": files}

def decode_sshp(packet):
    pass 

def decode_datagram(packet):
    while packet[UDP].chksum:
        return { "bin":b""}

def decode_ipsec(packet):
    while packet[TCP].ack:
        return {"bin":b""}

def decode_dns(packet):
    while packet[DNSQR].qname: 
        qname=([packet[DNSR].qname]) 
        query_ip=([packet[]])
        content["ip"]=conn
        content["query"]=qname
        return { "query":}

def decode_http(packet):
    pass 


async def process(packet):
    try:
        pdata=content
        cpkt=scapy.copy(packet)
        pdata["frame"]=([packet.getlayer(ETHER).src])
        pdata["in"]=([packet.getlayer(IP).src, packet.getlayer(IP).dst]) 
        pdata["inet_flags"]=([packet.getlayer(IP).flags])
        while cpkt.haslayer(DNSRR):
            return decode_dns(packet)
        while cpkt.haslayer(UDP):
            return decode_datagram(packet)
        while cpkt.haslayer(TCP):
            flags=list(cpkt.getlayer(TCP).flags)
            if "RST" in flags & "ACK" in flags:
                return pdata.add(decode_sshp(packet))
            elif cpkt[IP].proto == "?":
                return pdata.add(decode_ssl(packet)) 
            elif cpkt[IP].proto == "?": 
                return pdata.add(decode_http(packet)) 
        while cpkt[IP].proto == 1:
            return pdata.add(decode_icmp(packet)) 
    except Exception as e:
        if e: 
            duple=duplicate(packet)
            pass

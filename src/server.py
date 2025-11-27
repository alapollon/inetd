import protocol, ip, localproduct, remoteproduct, security, logger, pysftp, ssl, socket, collections, socketserver, typing, threading, multiprocessing, contextlib
from scapy.all import Ether, IP, TCP, DNS, UDP 
from collections import namedtuple, defaultDict

access=sockect
dserver=socketserver
context=contextlib
interfaces_address={}

frame=Ether
proto=IP 
rfc=TCP
name_services=DNS
datagram=UDP


from coroutine import Uplink, Downlink
class Cosocket(object):
    def __init__(self, soc, secure=False):
        self.protocol=soc
        self.secure=security()
        self.edge_weights=[None]
        pass
    def connect(self, target):
        if self.secure:
            secure_socket=Security.wrap_socket(self.switch, server_side= True)
            yield Uplink(secure_socket)
        else: 
            yield Uplink(self.protocol)
        yield self.protocol.connect(addr)
    def accept(self):
        yield Downlink(self.switch)
        if self.secure:
            try:
                data=self.secure_socket.read()
            except:
        else:
            conn, addr = self.protocol.accept()
            pass 

    def send(self, data):
        while dat 

class Base(declarative_base):
    def __init__(self, api):
        self.engine= create_engine(api)
        self.session=Session
        self.meta= MetaData(bind=self.engine)
        self.arrange=registry()

class UserDatabase(Base):
    def __init__(self, args):
        super(f'{socket.gethostname()}.database', localproduct( args.get['localdata']), remoteproduct(args.get['remotedata'])).__init__()
            
        pass
    
  

class LocalProduct(Userdatabase):
    def __init__(self, api):
        super().__init__()
        self._online_url={'localhost': '', 'localport':0}

        pass

def __init__():
        self._timing={ "localhost": asyncio.run(timing.start()) } 
        self._local_arp_table={}
        self.local_name



def spoof(self, target: string):

        

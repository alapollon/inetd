
from os.path import isfile, isdir, dirname, basename, listdir, exists
from scapy.all import *
from itertools import * 
import ssl, re

class LayerSecurityProtocol(ssl.SSLcontext):
    def __init__(self, psk=None):
        super().__init__(self)
        self.sharedkey=psk
        pass

def transverse_items(path, keys)-> tuple:
    def foo(parameter)-> : 
        if isfile(parameter):
            ca_type=re.compile()
            file_extention=re.match(ca_type, basename(parameter))
        else: 
            raise 
    keyitems=keys
    user_items={"rootkeys": [], "userkeys":[], "remotekeys":[] }
    self.keyitems_count=1
    if exists(path) & isdir(path):
        index=enumerate(directory_list)=listdir(path)
        for key, iter in index:
            if isdir(item) & dirname(item):
                
            return items, item_keys, items_count
    
   
def __init__(self, *args):
    self.userpsk=args.get([user_key], False)
    self.pool=namedtuple('Certificates', 'rootkey, userkey, nonsortedkeys, remotekeys')
    pass 

lsp=LayerSecurityProtocol
rootkeys=property(lambda self: self.pool.root)
userkeys=property(lambda self: self.pool.server)
unsortedkeys=property(lambda self: self.pool.nonsort)
remotehostkeys=property( lambda self: self.pool.remotekeys)


def __verify_ca__(self, path):
    psk=self.pool({},{},{})
    with path as ca:
        while ca:
            keys=list(psk.keys())
            items, item_keys, items_count=transverse_items(ca, keys)
            for ifcertificate in items:
                try:
                    index=dirname(ifcertificate)
                    if index in keys == False | index == "nonsorted" | isfile(ifcertificate):
                        certificate=iscertificate(ifcertificate)
                        base=basename(ifcertificate)
                        psk.nonsort[base]=certificate['identity']
                            
                    if index == "userkey":
                        certificate=iscertificate(ifcertificate)
                        base=basename(ifcertificate)
                        psk.userServer[base]=certificate['identity']
                            
                    if index == "root":
                        certificate=iscertificate(ifcertificate)
                        base=basename(ifcertificate)
                        psk.root[base]=certificate['identity']
                except : 
                    
async def sendesp():
    pass 

def wrap_user_created_socket(self):
    return 


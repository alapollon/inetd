import typing, logger, ssl, collections, iscertificate, 
from scapy.all 
from os.path import isfile, isdir, dirname, basename, listdir, exists


def __init__(self, *args):
    self.userpsk=args.get([user_key], False)
    self.pool=namedtuple('Certificates', 'root, server, nonsort')
    pass 

def transverse(path, keys)-> tuple:
        items_key=[]
        items=()
        items_count=1
        directory=[None]
        if exixts(path) & isdir(path):
            directory+=listdir(path)
            for item in directory:
                while isdir(item):
                    d2=listdir(item)
                    head= i = dirname(item) if i in keys 
                    keys+=head
                    items+=
                    items_count=len(items)
                    continue
                while isfile(item):
                    item_keys+= basename(item)
                    items+=item
                    items_count+=1
                    continue
                if isfile(item) == False & isdir(item) == False:
                        continue
                return items, item_keys, items_count
        elif isfile(path):
            keys+=basename(path)
            return items, keys, items_count

def __verify_server_ca__(self, path):
    psk=self.pool({},{},{})
    with path as ca:
        while ca:
            keys=list(psk.keys())
            items, item_keys, items_count=transverse(ca, keys)
            for ifcertificate in items:
                    index=dirname(ifcertificate)
                    while index in keys == False | index == "nonsorted" | isfile(ifcertificate):
                            try:
                                certificate=iscertificate(ifcertificate)
                                base=basename(ifcertificate)
                                psk.nonsort[base]=certificate['identity']
                            except Exception as e:
                                pass
                    while index == "userServer":
                            try:
                                certificate=iscertificate(ifcertificate)
                                base=basename(ifcertificate)
                                psk.userServer[base]=certificate['identity']
                            except Exception as e:
                                pass
                    while index == "root":
                        try:
                            certificate=iscertificate(ifcertificate)
                            base=basename(ifcertificate)
                            psk.root[base]=certificate['identity']
                        except Exception as e:
                            pass

rootkeys=property(lambda self: self.pool.root)
userkeys=property(lambda self: self.pool.server)
unsortedkeys=property(lambda self: self.pool.nonsort)


class LSP(ssl.SSLcontext):
    def __init__(self, psk=None):
        super().__init__(self)
        self.
        pass









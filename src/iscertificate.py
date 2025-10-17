from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def __init__(self, path):
    self.filepath=path
    self.stats={}
    pass 

try: 
    with open(filepath, "rb") as item:
        signature=item.read()
        try:
            certificate=x509.load_pem_x509_certificate(signature)
            if certificate:
                self.stats['value']=True 
                self.stats['category']="pem"
                self.stats['identity']=certficate.serial_number
                return self.stats
        except (ValueError, FileNotFoundError) :
            if ValueError:
                pass
            else:
                return False
        try: 
            certificate=x509.load_der_x509_certificate(signature)
            if certificate:
                    self.stats['value']=True
                    self.stats['category']="der"
                    self.stats['identity']=str(certificate)
                    return self.stats
        except (ValueError, FileNotFoundError) :
            if ValueError:
                return False
except Exception as e:



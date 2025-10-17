import socket, time, struct


def __init__(self, object, count_seconds: int, domainserver=None ) :
    self.socket=object
    self.timeout= count_seconds if count_seconds  >= 1 else None

def target(self):
    

try:
    time_out=self.timeout
    

    ICMP=socket.getprotobyname('icmp')
    UDP=socket.getprotobyname('udp') 

    icmp_sock=socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP) 
    udp_sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, UDP)

    timeout_struct= struct.pack() 
    icmp.sock.fromfd(
    icmp_sock.setsockopt() 

except:

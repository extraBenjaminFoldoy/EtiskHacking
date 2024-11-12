import random
import time
from scapy.all import *

target_ip = "192.168.0.138"
port_range = range(20, 1024)

ip = IP(dst=target_ip)

for port in port_range:
    syn = TCP(dport=port, flags="S")
    packet = ip / syn
    send(packet)
    
    delay = random.uniform(1, 4)
    print(f"scanning port {port} \n delat {delay:.2f}s")
    time.sleep(delay)

print("DONE!")

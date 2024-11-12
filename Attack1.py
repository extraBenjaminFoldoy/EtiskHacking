from scapy.all import *

target_ip = "192.168.0.138"
target_port = 80

ip = IP(dst=target_ip)
icmp = ICMP()

fragmented_icmp = ip / icmp

send(fragmented_icmp)
from worker import app
from scapy.all import *
import ipaddress




@app.task(name='pinger.ping_host')
def ping_host(host: str, timeout=2):
    packet = IP(dst=host)/ICMP()
    reply = sr1(packet, timeout=timeout)
    if reply:
        return reply.summary()
    return f'Destination "{host}" not reachable.'

@app.task(name='pinger.discover')
def discover(subnet: str, timeout=2):
    ips = [str(ip) for ip in ipaddress.IPv4Network(subnet)]
    reachable = []
    for ip in ips:
        packet = IP(dst=ip)/ICMP()
        reply = sr1(packet, timeout=timeout)
        if reply:
            reachable.append(ip)
    return reachable
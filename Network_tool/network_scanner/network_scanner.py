#!/usr/bin/env python

from scapy.layers.l2 import Ether,ARP
import scapy.all as scapy

def scan(ip):
    #scapy.arping(ip)
    arp_req = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_req_bc = broadcast/arp_req
    ans_lst = scapy.srp(arp_req_bc, timeout=1,verbose=False)[0]
    #srp => sent & receive package
    print("        IP\t\t  MAC Address\n"+"-"*50)
    client_list =[]
    for x in (ans_lst):
        client_dict = {"ip": x[1].psrc, "mac": x[1].hwsrc}
        client_list.append(client_dict)
        # print("     "+x[1].psrc+"\t      "+x[1].hwsrc)
        # hwsrc & psrc are the source the sending to us
    return (client_list)

def print_list_of_dicts(lst):
    #this function made for print list of dicts.
    for x in (lst):
        print("     "+x["ip"]+"\t      "+x["mac"])


print_list_of_dicts(scan('10.0.2.1/24'))
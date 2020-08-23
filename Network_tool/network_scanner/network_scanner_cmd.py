#!/usr/bin/env python

#pip3 install scapy-python3
from scapy.layers.l2 import Ether,ARP
#in python 3 -> argparse & argparse.ArgumentParser()
#parser.add_argument
import optparse
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

def getip():
    parser = optparse.OptionParser()
    parser.add_option("-i","--ip",dest="ip",help="Enter your ip range : ")
    #Ex. 10.0.2.1/24 :
    option = parser.parse_args()[0]
    if (not option.ip):
        parser.error("[-] Please specify an IP Address. use --help for more info.")
    return option.ip


print_list_of_dicts(scan(getip()))
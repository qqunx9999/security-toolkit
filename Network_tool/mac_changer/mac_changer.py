#!/usr/bin/env python
#eth0_initial = 08:00:27:5b:b1:a6
import re
import subprocess
import optparse

def getarg():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (option,argument) = parser.parse_args()
    if (not option.interface or not option.new_mac):
        parser.error("[-] Please specify an interface. use --help for more info.")
    return option


def change_mac(itf,nm):
    print("[+] Changing MAC Adress for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", itf ,"down"])
    subprocess.call(["ifconfig", itf, "hw", "ether", nm])
    subprocess.call(["ifconfig", itf, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_result:
        return mac_result.group(0)
    else:
        pass

#dest = "interface" <<that's mean the values from user will keep in variable interface
option = getarg()
interface = option.interface
new_mac = option.new_mac
change_mac(interface,new_mac)
c_mac = get_current_mac(interface)
if c_mac == new_mac:
    print("[+] Change MAC Address successfully to "+new_mac)
else:
    print("[-] Cannot access the MAC Address ")


#number in arg group(x); <-- x is the NO. of seq. matching

#eth0_initial = 08:00:27:5b:b1:a6

# subprocess.call(["ifconfig "+interface+" down",shell=True)
# subprocess.call("ifconfig "+interface+" hw ether "+new_mac,shell=True)
# subprocess.call("ifconfig "+interface+" up",shell=True)

#Part two check program work perfectly
import os
import platform
import re

host_window = r"C:\Windows\System32\drivers\etc\hosts"
host_mac = r"/etc/hosts"


HOST_LIVE = ["#dcalc",
             "127.0.0.1:17173       www.dcalc.com"]

def search_host(hostvalue):
    if platform.system().lower() != "windows":
        host_path = host_mac
    else:
        host_path = host_window
    hostfile = open(host_path, 'r',errors='ignore')
    each_line = hostfile.readlines()
    hostfile.close()
    findresult = re.findall(hostvalue, ''.join(each_line))
    return findresult

def write_host(hostvalue):
    if platform.system().lower() != "windows":
        output = open(host_mac, 'a')
    else:
        output = open(host_window, 'a')

    for insid in hostvalue:
        output.write(insid)
        output.write("\n")
    output.close()

def host_init():
    if not search_host(HOST_LIVE[0]):
        write_host(HOST_LIVE)
"""
Author:LuckyRiver
Date:2021
主机爆破
"""
from scapy.all import *
from optparse import OptionParser


def scan_host(ip):
    pkt = IP()/ICMP(seq=2000)/b'hello world'
    pkt['IP'].dst = ip
    results = sr1(pkt,timeout=1,iface = IFACES.dev_from_index(7),verbose=0)
    if results:
        print( '[+] host: %s is up '%ip)

if __name__ == "__main__":
    opt = OptionParser("usage: %prog -i ip or ips")
    opt.add_option("-i", '--IP', type="string", dest="ips", help="input ip or ips")
    options, args = opt.parse_args()
    # ips = options.ips
    ips = input("输入ips:  ")


    if "-" in ips:
        start_ip = ips.splie("-")[0]
        start_num = int(start_ip(".")[-1])
        end_num = int(ips_split("-")[1])
        for num in range(start_num,end_num+1):
            tmp = start_ip.spilt(".")
            ip = tmp[0]+"."+tmp[1]+"."+tmp[2]+"."+str(num)
            scan_host(ip)
    else:
        scan_host(ips)

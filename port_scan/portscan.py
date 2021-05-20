"""
端口扫描
"""
import socket
import threading
from optparse import OptionParser
from concurrent.futures import ThreadPoolExecutor



def scan_one(ip,port):

    # ip = "192.168.10.151"
    # port = 80
    socket.setdefaulttimeout(1)
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((ip,port))
        print("[+] %d is open" % port)

    except:
        # print("[+] %d is closed" % port)
        pass

if __name__ == "__main__":
    opt = OptionParser("usage: %prog -i IP -p PORT")
    opt.add_option("-i", "--IP", type='string', dest='ip', help="scan ip address")
    opt.add_option('-p', '--PORT', type="string", dest='port', help="scan port or ports")
    opt.add_option('-t', '--Thread', type="int", dest='threads', help="thread numbers ")

    options, args = opt.parse_args()
    ip = options.ip
    ports = options.port
    if not ip:
        print("请使用-h参数查看帮助")
    else:
        if "-" in ports:
            start_port = int(ports.split("-")[0])
            end_port = int(ports.split("-")[1])
            thread_num = options.threads
            with ThreadPoolExecutor(max_workers=thread_num) as pool:
                for port in range(start_port,end_port+1):
                    pool.submit(scan_one,ip,port)
        else:
            scan_one(ip,int(ports))

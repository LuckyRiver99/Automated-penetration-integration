"""
Author:LuckyRiver
Date:2021
管理所有脚本
"""
import os
import re

def use_module(module):
    while True:
        command = input("LuckyRiver>(%s) "%module)
        dirs = tdict[module]
        if command.strip() == 'exit':
            break
        if re.match('^run ', command.strip()):
            patt = re.compile('^run (.*)')
            para = re.findall(patt, command)[0].strip()
            cc = "python %s %s" % (dirs, para)
            print(cc)
            result = os.popen(cc)
            for item in result:
                print(item.strip())
        elif command.strip() != "":
            cc = "python %s -h" % (dirs)
            print(cc)
            result = os.popen(cc)
            print("="*50)
            print("在参数前加 run ,不需要写xxx.py文件")
            print("Example: run -h")
            for item in result:
                print(item.strip())

tool_dict = {
    "baidu_domain":"baidu_domain",
    "force_domain":"force_domain",
    "port_scan":"port_scan",
    "mysql_brute":"mysql_brute",
    "host_scan":"host_scan",
    "01":"baidu_domain",
    "02":"force_domain",
    "03":"port_scan",
    "04":"mysql_brute",
    "05":"host_scan"
}
tdict = {
    "baidu_domain":"scan_domain/baidu_domain.py",
    "force_domain":"scan_domain/force_domain.py",
    "port_scan":"port_scan/portscan.py",
    "mysql_brute":"mysql_brute/mysql_brute.py",
    "host_scan":"host_scan/scapy-sniff.py"
}

print("Welcome Lr's tools!")
print("01 先输入域名 换行后输入page数字")
print("02 输入网站域名 即可子域名进行破解")
print("03 支持多线程定义 开放端口号显示")
print("04 先输入主机 换行后输入端口连接 ")
print("05 先输入ip 换行后输入端口范围查看 ")

while True:
    cmd = input("LuckyRiver> ")
    if cmd == "?" or cmd == "help":
        print("="*50)
        print("Usage:")
        print("command    description")
        print("ls        :list all module")
        print("pwd       :print work directory")
        print("use       :choice module")
        print("exit      :exit tools")
    elif cmd.strip() == "ls":
        print("="*50)
        print("Usage: use <tool name>")
        print("01:\tbaidu_domain\n02:\tforce_domain\n03:\tport_scan\n04:\tmysql_brute\n05:\thost_scan")
        print("-"*50)
        print("exmaple: use 01")
        print("         use baidu_domain")
    elif cmd == "pwd":
        print(os.getcwd())
    elif re.match('^use ',cmd.strip()):
        pattern = re.compile('^use (.*)')
        module = re.findall(pattern,cmd)[0].strip()
        modules = ["baidu_domain","force_domain","port_scan","mysql_brute","host_scan","01",
                   "02","03","04","05"]
        if module in modules:
            use_module(tool_dict[module])
    elif cmd.strip('') == "exit":
        # status = False
        break


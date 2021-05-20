"""
Author:LuckyRiver
Date:2021
通过暴力破解来获得子域名，类似子域名挖掘机的功能
"""
import requests
from concurrent.futures import ThreadPoolExecutor
from optparse import OptionParser

def mingan_domain(key,domain):

    url = "https://" + key + '/' + domain
    # url = "https://www.baidu.com/calc_8.php"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    try:
        resp = requests.get(url=url,headers=headers)
        if resp.status_code==200:
            print(url)
            with open("./iwanti.txt", 'ab+') as s:
                s.write((url + '\n').encode("utf-8"))
    except:
        pass

if __name__ == '__main__':
    opt = OptionParser("usage: %prog -i ip or ips")
    opt.add_option("-u", '--key', type="string", dest="key", help="input yuming")
    opt.add_option("-t", '--threads', type="int", dest="threads", help="thread number")
    options, args = opt.parse_args()
    # key = input("请输入域名: ")
    # t = input("请输入")
    key = options.key
    thread_num = options.threads
    with open("../PHP.txt", 'r') as f:
        domain = f.readline().strip()
        with ThreadPoolExecutor(max_workers=options.threads) as pool:
            while domain:
                pool.submit(mingan_domain,key,domain)
                domain = f.readline().strip()


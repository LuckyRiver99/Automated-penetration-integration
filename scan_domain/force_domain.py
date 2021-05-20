"""

Author:LuckyRiver
Date:2021
通过暴力破解来获得子域名，类似子域名挖掘机的功能

"""
import requests
from concurrent.futures import ThreadPoolExecutor


def scan_domain(key,domain):
    url = "https://" + key + "." + domain
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            print(url)
            with open("./iwant.txt", 'ab+') as s:
                s.write((url+'\n').encode("utf-8"))
    except:
        pass




if __name__ == '__main__':
    domain = input("请输入网站:  ")
    with open('../dic.txt', 'r') as f:
        key = f.readline().strip()
        with ThreadPoolExecutor(max_workers=100) as pool:
            while key:
                pool.submit(scan_domain, key, domain)
                key = f.readline().strip()

"""
Author:LuckyRiver
Date:2021
1、通过必应 ，爬取一页的子域名信息
2、随意输入需要查询的域名,得到子域名
3、可以爬取必应搜索中的多页内容
"""
import requests
import re
from optparse import OptionParser
#查询子域名
def scan_domain(domain,page):
    sub_domains = []#空集合
    for i in range(2,page):
        url = "https://cn.bing.com/search?q=site:%s&first=%d" % (domain, 5+10*(i-2))
        headers = {

            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        html_str = response.text
        pattern = re.compile('<cite>(.*?)</cite>')
        # pattern2 = pattern.replace('<strong>','')
        # pattern3 = pattern2.replace('<','')
        results = re.findall(pattern, html_str)
        # print(results)

        for res in results:
            if "." in res:
                if "/" in res:
                    sub_d = res.split('/')[0]
                    sub_domains.append(sub_d)
    return sub_domains

if __name__ == "__main__":
    opt = OptionParser("usage: %prog -i ip or ips")
    opt.add_option("-d", '--domain', type="string", dest="domain", help="input yuming")
    opt.add_option("-p", '--page', type="int", dest="page", help="page number")
    options,args = opt.parse_args()
    domain = options.domain
    page = options.page
    # domain = input("输入")
    # page = int(input("输入"))
    sub_domains = scan_domain(domain,page)
    print(sub_domains)

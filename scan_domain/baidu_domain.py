"""
Author:LuckyRiver
Date:2021
1、通过百度搜索 toutiao.com ，爬取一页的子域名信息
2、随意输入需要查询的域名,得到子域名
3、可以爬取百度搜索中的多页内容
4、使用多线程,加快子域名爬取速度
5、子域名写入到subdomain/domain.txt
"""
import requests
import re

#查询子域名
def scan_domain(domain,p):
    sub_domains = []#空集合
    for i in range(p):
        url = "https://www.baidu.com/s?wd=site:%s&pn=%d" % (domain, i * 10)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        }
        response = requests.get(url=url, headers=headers)
        html_str = response.text
        pattern = re.compile('class="c-showurl c-color-gray".*?>(.*?)<')
        results = re.findall(pattern, html_str)
        # print(results)

        for res in results:
            if "." in res:
                if "/" in res:
                    sub_d = res.split('/')[0]
                    sub_domains.append(sub_d)
    return sub_domains

if __name__ == "__main__":
    domain = input("input scan domain:")
    p = int(input("input scan page:"))
    sub_domains = scan_domain(domain,p)
    print(sub_domains)

# -
(1)信息收集 端口 主机 子域名（爆破、爬虫 )(百度、必应) 目录扫描 御剑  (2)爆破  (3)mysql服务

# 前言
本周python复习阶段，做了一个集成性的poc脚本用来测试网站、服务器子域名，mysql远程登录，端口、IP扫描探测
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210227224112923.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3hpbnl1ZTk5NjY=,size_16,color_FFFFFF,t_70)


# 百度查找子域名
写了正则.*?   
.表示除\n之外的任意字符
*表示匹配0-无穷
?表示懒惰匹配
前两个一起.*是贪婪匹配，尽可能多的匹配所有，(. * ？)就是匹配尽可能少的字符。就意味着匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复。


"""
Author:LuckyRiver
Date:2021
1、通过百度搜索 toutiao.com ，爬取一页的子域名信息
2、随意输入需要查询的域名,得到子域名
3、可以爬取百度搜索中的多页内容
4、使用多线程,加快子域名爬取速度
"""


# 暴力破解子域名

"""
Author:LuckyRiver
Date:2021
通过暴力破解来获得子域名，类似子域名挖掘机的功能


# namp类端口开放扫描
port值在传输时是int类型 不能使用引号

"""
Author:LuckyRiver
Date:2021
1、指定ip和端口进行探测
2、使用命令行参数
3、多个端口扫描
4、使用多线程，并且用户可以控制线程数量
"""


# MySQL远程登录
写入绝对路径，端口多为3306，如果修改可以在sql命令行中使用进行查询

> show global variables like 'port';



"""
Author:LuckyRiver
Date:2021
数据库爆破
"""


# scapy类IP扫描
type类型注意是string，iface使用为了连接802.11ac端口，需要人为查找，方法是进入scapy模块输入

> ifaces

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021022722101123.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3hpbnl1ZTk5NjY=,size_16,color_FFFFFF,t_70)




"""
Author:LuckyRiver
Date:2021
主机发现：使用ICMP探测
1、使用Scapy，指定一个IP进行探测
2、探测多个IP是否活跃
3、使用命令行参数输入 类似于 nmap工具使用 xxx.py -i ip （支持多个ip扫描）
4、多线程扫描
"""


# 集成界面
文件路径在cmd中需要使用绝对路径

# 后记
本工具实现5个功能性模块，不过暂未实现键盘暂停任务，文件名需要自定义后修改文件目录，绝对路径和相对路径对于cmd是否能够识别起了很大作用，祝大家使用愉快！有些bug希望老哥们给提提意见，包括python中键盘键操作搜索了很多，也没什么思路，欢迎各位老哥指教!

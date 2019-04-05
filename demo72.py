#代理池的获取，存储，检测
#https://www.xicidaili.com/nt/1   本次仅西刺代理，第一页，尝试下
#被封ip了，不让访问了，下次，还是取到ip后直接json格式保存吧，demo74即可了
import random   #随机模块
import requests
from lxml import etree

header = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('https://www.xicidaili.com/nt/1', headers=header)
request.encoding = 'utf-8'
x = request.text
# print(x)
html = etree.HTML(x)
xip = html.xpath('//table[@id="ip_list"]//tr/td[2]/text()')   #获取ip
# print(xip)
xdk = html.xpath('//table[@id="ip_list"]//tr/td[3]/text()')   #获取端口号
# print(xdk)
dictionary = list(zip(xip, xdk))
# print(dictionary)
ip_list = []
for i in dictionary[:3]:
    i2 = ':'.join(i)    #拼接为219.245.3.4:3128形式字符串
    ip_list.append(i2)  #放进列表里，便于random随机模块取用

print(ip_list)
ip_ran = random.choice(ip_list) #随机取ip地址


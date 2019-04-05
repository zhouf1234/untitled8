import requests
import re
import json
from lxml import etree
import os

# proxy = {
#     "http":"110.52.235.217:9999",   #使用89网获取的这个可用ip地址
# }

# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# shouyao = requests.get('http://www.1kkk.com/manhua11276/',headers=header)
# sh = shouyao.text
#
# html = etree.HTML(sh)
# bburl = html.xpath('//div[@id="chapterlistload"]//ul[1]//li/a/@href')
# # print(bburl)    #所有分页面url,虽然时反向的
# bburl2 = []
# for bu in bburl:
#     bur = {'url':'http://www.1kkk.com'+bu}
#     bburl2.append(bur)
# print(bburl2)
# # 将bburl2的json文本以json序列化的方法写进,下载所有分页面的url存进json文件先
# with open('bburl.json', 'w')as file:
#     file.write(json.dumps(bburl2, indent=2))

#读取bburl这个json文件的所有url,并反转列表
url_list = []
with open('bburl.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    for u in dat:
        url_list.append(u['url'])
url_list.reverse()
print(url_list)
import requests
import re
import json
from lxml import etree
import os

#不写user-agent，不换ip地址，不一步步爬取，会被网站发现是爬虫
#先取得所有分页面的url保存成json文件
#读取json文件的所有url，更换ip，爬取所有章节内容并保存为json文件
#最后把章节内容的json文件保存为120个txt文件。

# proxy = {
#     "http":"223.93.145.186:8060",   #使用89网获取的这个可用ip地址
# }

# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# shouyao = requests.get('http://book.zongheng.com/showchapter/477645.html',headers=header,proxies=proxy)
# sh = shouyao.text
#
# s = re.compile('<div.*?class="volume-list">.*?<div>.*?<ul.*?>(.*?)</ul>.*?</div>.*?</div>',re.S)
# title = re.findall(s,sh)
# for tit in title:
#     s2 = re.compile('<a.*?href="(.*?)".*?>')
#     title2 = re.findall(s2,tit)
#     # print(title2[:2])       #所有章节url
#     jsonurl2 = []
#     for ju in title2:
#         jsonurl = {'url':ju}
#         jsonurl2.append(jsonurl)
#     print(jsonurl2)
#     # 将jsonurl2的json文本以json序列化的方法写进,下载所有分页面的url存进json文件先
#     with open('jsonurl.json', 'w')as file:
#         file.write(json.dumps(jsonurl2, indent=2))

#读取jsonurl这个json文件的所有url
url_list = []
with open('jsonurl.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    for u in dat:
        url_list.append(u['url'])
# print(url_list)

# writes = []
# for url in url_list:
#     # print(url)
#     proxy2 = {
#         "http": "58.56.108.226:58690",  # 使用89网获取的这个可用ip地址
#     }
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
#     shouyao1 = requests.get(url, headers=header, proxies=proxy2)
#     sh1 = shouyao1.text
#
#     # s3 = re.compile('<div.*?class="title">.*?<div.*?class="title_txtbox">(.*?)</div>',re.S)
#     # biaoti = re.findall(s3,sh1)
#     # print(biaoti)     #章节标题,并不需要，注释掉
#
#     html = etree.HTML(sh1)
#     write = html.xpath('//div[@class="content"]//p//text()')
#     # print(write)      #章节内容
#     write2 = ','.join(write)
#     # print(type(write2))
#     write3 = {'nr': write2}
#     writes.append(write3)

# 存储章节内容，json格式
# with open('nrws.json', 'w')as file:
#     file.write(json.dumps(writes, indent=2,ensure_ascii=False))

#读取json文件并保存为txt文件
with open('nrws.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    # print(len(dat)) #长度120，说明内容都爬取下来了
    for nr in range(len(dat)):
        # print(nr)
        write4 = dat[nr]['nr']
        write5 = write4.split(',')  #字符串分割为列表，使保存时不粘连，一行一行存
        for wr in write5:
            # print(wr)
            filepath = './shouyao'
            if not os.path.exists(filepath):  # 如果文件夹不存在就创建
                os.mkdir(filepath)
            p2 = filepath + '/%s.txt' % nr
            # print(p2)
            # with open(p2, "a")as f:
            #     f.write(wr + '\n')           #保存为120个txt文件
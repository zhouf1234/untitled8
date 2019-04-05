import requests
import re
import json
from lxml import etree
import os

# proxy = {
#     "http":"110.52.235.217:9999",   #使用89网获取的这个可用ip地址
# }
#
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# shouyao = requests.get('http://book.zongheng.com/showchapter/92371.html',headers=header,proxies=proxy)
# sh = shouyao.text
#
# s = re.compile('<div.*?class="volume-list">.*?<div>.*?<ul.*?>(.*?)</ul>.*?</div>.*?</div>',re.S)
# title = re.findall(s,sh)
# for tit in title:
#     s2 = re.compile('<a.*?href="(.*?)".*?>')
#     title2 = re.findall(s2,tit)
#     print(title2)       #所有章节url
#     jsonurl2 = []
#     for ju in title2:
#         jsonurl = {'url':ju}
#         jsonurl2.append(jsonurl)
#     print(jsonurl2)
#     # 将jsonurl2的json文本以json序列化的方法写进,下载所有分页面的url存进json文件先
#     with open('lmjurl.json', 'w')as file:
#         file.write(json.dumps(jsonurl2, indent=2))

#读取jsonurl这个json文件的所有url
url_list = []
with open('lmjurl.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    for u in dat:
        url_list.append(u['url'])
# print(url_list)

# writes = []
# for url in url_list:
#     # print(url)
#     proxy2 = {
#         "http": "119.101.114.198:9999",  # 使用89网获取的这个可用ip地址
#     }
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
#     shouyao1 = requests.get(url, headers=header, proxies=proxy2)
#     sh1 = shouyao1.text
#
#     html = etree.HTML(sh1)
#     write = html.xpath('//div[@class="content"]//p//text()')
#     # print(write)      #章节内容
#     write2 = ','.join(write)
#     # print(type(write2))
#     write3 = {'lmj': write2}
#     writes.append(write3)
#
# # 存储章节内容，json格式，已保存成功
# with open('lmjs.json', 'w')as file:
#     file.write(json.dumps(writes, indent=2,ensure_ascii=False))

#读取,并保存为txt文件
with open('lmjs.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    # print(len(dat)) #长度83，说明内容都爬取下来了
    for nr in range(len(dat)):
        # print(nr)
        write4 = dat[nr]['lmj']
        write5 = write4.split(',')  #字符串分割为列表，使保存时不粘连，一行一行存
        for wr in write5:
            # print(wr)
            filepath = './lingmojie'
            if not os.path.exists(filepath):  # 如果文件夹不存在就创建
                os.mkdir(filepath)
            p2 = filepath + '/%s.txt' % nr
            # print(p2)
            # with open(p2, "a")as f:
            #     f.write(wr + '\n')           #保存为83个txt文件
import requests
import re
from lxml import etree
import json

# proxy = {
#     "http":"223.93.145.186:8060",   #使用89网获取的这个可用ip地址
# }
#
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# shouyao1 = requests.get('http://book.zongheng.com/chapter/477645/8258219.html',headers=header,proxies=proxy)
# sh1 = shouyao1.text
# # print(sh1)
#
# html = etree.HTML(sh1)
# write = html.xpath('//div[@class="content"]//p//text()')
# # print(write)
# write2 = ','.join(write)
# # print(type(write2))
# write3 = {'nr':write2}
#存储
# with open('nr.json', 'w')as file:
#     file.write(json.dumps(write3, indent=2,ensure_ascii=False))

#读取,并保存为txt文件
with open('nr.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    # print(dat)
    write4 = dat['nr']
    write5 = write4.split(',')
    # print(write5)
    for wr in write5:
        print(wr)
        # with open('nr2.txt', 'a', encoding='utf-8') as f:
        #     f.write(wr + '\n')
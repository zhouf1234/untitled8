import requests
import re
from lxml import etree
import json

# proxy = {
#     "http":"110.52.235.217:9999",   #使用89网获取的这个可用ip地址
# }
#
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# shouyao1 = requests.get('http://book.zongheng.com/chapter/92371/2223280.html',headers=header,proxies=proxy)
# sh1 = shouyao1.text
# # print(sh1)
#
# html = etree.HTML(sh1)
# write = html.xpath('//div[@class="content"]//p//text()')
# # print(write)
# write2 = ','.join(write)
# print(write2)
# write3 = {'lmj':write2}
# # 存储
# with open('nr3.json', 'w')as file:
#     file.write(json.dumps(write3, indent=2,ensure_ascii=False))

#读取,并保存为txt文件
with open('nr3.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    print(dat)
#     write4 = dat['lmj']
#     write5 = write4.split(',')
#     # print(write5)
#     for wr in write5:
#         print(wr)
        # with open('nr4.txt', 'a', encoding='utf-8') as f:
        #     f.write(wr + '\n')
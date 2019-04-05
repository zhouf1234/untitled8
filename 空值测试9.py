import requests
import re
from lxml import etree
import json
import os

# proxy = {
#     "http":"119.101.114.198",   #使用89网获取的这个可用ip地址
# }
#获取24个url，24话,同样面临被封ip的问题
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# banben = requests.get('http://comic.kukudm.com/comiclist/2051/',headers=header)
# bb = banben.text
# # print(bb)
# htm = etree.HTML(bb)
# bburl = htm.xpath('//dl[@id="comiclistn"]//dd/a[1]/@href')
# # print(bburl)    #所有话的url
# baben = []
# for bu in bburl:
#     bj = {'bu':'http://comic.kukudm.com'+bu}
#     baben.append(bj)
#     with open('banben.json', 'w')as file:
#         file.write(json.dumps(baben, indent=2))

#读取jsonurl这个json文件的所有url
url_list = []
with open('banben.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    for u in dat:
        url_list.append(u['bu'])
print(url_list[1][:-5])     #一话一话来吧，图片确实太多了

# bimage = []
# for i in range(1,36):  #设定一个固定页数值，如果响应码是200，就爬取内容，不用找页数了，电脑太卡不用这个
#     # url = 'http://comic.kukudm.com/comiclist/2051/43657/' +str(i) +'.htm'
#     url = url_list[0][:-5] +str(i) +'.htm'
#     # print(url)
#     header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
#     banb = requests.get(url,headers=header)
#     # if banb.status_code ==200:
#     sh1 = banb.text
#     # print(sh1)
#     html = etree.HTML(sh1)
#     burl = html.xpath('//table[2]//tr//td//script[@language="javascript"]/text()')
#     for bu in burl:
#         # print(bu)
#         bu2 = re.compile('<IMG.*?SRC=(.*?)>.*?<span.*?>',re.S)
#         bu3 = re.findall(bu2,bu)
#         # print(bu3)
#         for bu4 in bu3:
#             bu5 = re.sub('.*?/ÎÒ½ÐÛà±¾ÎÒ×î\x8cÅ|\'','',bu4)
#                 # bu5 = re.sub('.*?/|\'','',bu4)
#             bu6 = {'bb':'http://n5.1whour.com/newkuku/2014/201412/1220b/我叫坂本我最屌/'+bu5}
#             print(bu6)
#             bimage.append(bu6)
            # with open('bbimg.json', 'w')as file:
            #     file.write(json.dumps(bimage, indent=2))

with open('bbimg.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    # for u in dat:
    #     print(u['bb'])
    for i in range(len(dat)):
        print(dat[i]['bb'])
        header = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        banb = requests.get(dat[i]['bb'], headers=header)
        filepath = './banben/02'
        if not os.path.exists(filepath):  # 如果文件夹不存在就创建
            os.mkdir(filepath)
        p2 = filepath + '/%s.jpg' % i
        # print(p2)
        with open(p2, "wb+")as f:
                f.write(banb.content)

#正确图片地址：'http://n5.1whour.com/newkuku/2014/201412/1220b/我叫坂本我最屌/Vol_1//0001IG9.jpg'

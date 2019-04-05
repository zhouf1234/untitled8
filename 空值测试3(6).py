import requests
import re
from lxml import etree
import json

# proxy = {
#     "http":"110.52.235.217:9999",   #使用89网获取的这个可用ip地址
# }
#分页面页数，去分页面取图片，图片是以js脚本导入的，目前无法爬取。。
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# shouyao1 = requests.get('http://www.1kkk.com/ch1-121840/',headers=header)
# sh1 = shouyao1.text
# # print(sh1)
#
# html = etree.HTML(sh1)
# urlpage = html.xpath('//div[@class="chapterpager"]/a[last()]/text()')
# # urlpage2 = urlpage[0]
# urlpage3 = str(urlpage[0])
# # print(type(urlpage3))
# # print(type(urlpage))
# for i in range(1,int(urlpage3)+1):
#     #http://www.1kkk.com/ch1-121840/#ipg30  #
#     iurl = 'http://www.1kkk.com/ch1-121840/'+'#ipg'+str(i)
#     print(iurl)

# header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
#         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Encoding':'gzip, deflate, sdch',
#         'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
#         'Cache-Control':'no-cache',
#         'Connection':'keep-alive',
#         'Cookie':'frombot=1; DM5_MACHINEKEY=7d32c3b7-43c3-4bf3-b0d5-d4ebb00a7a3b; SERVERID=node3; UM_distinctid=1683fcc84b72a3-08e01de0bb4fc8-b781636-100200-1683fcc84b8547; __utmc=1; __utmz=1.1547258595.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; CNZZDATA1258751965=1941341054-1547257106-http%253A%252F%252Fwww.1kkk.com%252F%7C1547257106; dm5cookieenabletest=1; CNZZDATA1261430601=761267674-1547255799-http%253A%252F%252Fwww.1kkk.com%252F%7C1547272442; CNZZDATA1258752048=165810239-1547258387-http%253A%252F%252Fwww.1kkk.com%252F%7C1547274589; CNZZDATA1258751996=1535362569-1547254846-http%253A%252F%252Fwww.1kkk.com%252F%7C1547271048; dm5imgcooke=124685%7C2%2C219145%7C2%2C121840%7C30%2C121901%7C22; firsturl=http%3A%2F%2Fwww.1kkk.com%2Fch1-121840%2F; CNZZDATA30046992=cnzz_eid%3D1682363605-1547256493-null%26ntime%3D1547278344; CNZZDATA1258880908=807440980-1547253881-null%7C1547280881; __utma=1.1746099637.1547258595.1547272398.1547282122.3; __utmt=1; ComicHistoryitem_zh=History=11276,636829080043612143,121840,26,1,0,2,2&ViewType=1&OrderBy=2; readhistory_time=1-11276-121840-26; image_time_cookie=121840|636829080043767939|27,121901|636829017152061654|3; dm5imgpage=124685|1:1:55:0,121840|26:1:55:0,219145|1:1:55:0,121901|3:1:56:0; __utmb=1.6.10.1547282122',
#         'Host':'www.1kkk.com',
#         'Pragma':'no-cache',
#         'Referer':'http://www.1kkk.com/ch1-121840/',
#         'Upgrade-Insecure-Requests':'1'
# }
# banben = requests.get('http://www.1kkk.com/ch1-121840/#ipg1', headers=header)
# sh2 = banben.text
# print(sh2)
# html = etree.HTML(sh2)
#
# bbimge = html.xpath('//div[@class="view-main"]//div')
# print(bbimge)






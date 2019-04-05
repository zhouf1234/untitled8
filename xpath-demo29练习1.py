import requests
from lxml import etree

# 用xpath方法写
# 中华人民共和国 政策
# http: // www.gov.cn / zhengce /
# 最新政策标题

# 分析页面
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.gov.cn/zhengce/',headers=header)
request.encoding='utf-8'
c = request.text
# print(type(c))

html = etree.HTML(c)
res = html.xpath("//div[@class='list list_1']//ul//li//a/text()")
# print(res)
for i in res:
    print(i)

# 保存,终于按序保存成文件了
file=open("./files/最新政策.txt","w+")
for i in range (len(res)):
    file.write(res[i]+"\n")
file.close()
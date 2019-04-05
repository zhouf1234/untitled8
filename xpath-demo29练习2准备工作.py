import requests
from lxml import etree

# 用xpath方法写
# 中华人民共和国 政策
# http: // www.gov.cn / zhengce /
# 最新政策标题，二级目录的正文

# 分析页面
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.gov.cn/zhengce/',headers=header)
request.encoding='utf-8'
c = request.text

#取到所有网页的连接
# http://www.gov.cn/zhengce/2018-11/29/content_5344537.htm
# http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm,两种连接格式实际
# 只取href后面的连接的话，无法连接，有些无前缀，需要进行拼接
html = etree.HTML(c)
res = html.xpath("//div[@class='list list_1']//ul//li//a/@href")
# print(type(res))  #list类型
for i in res:
    print(type(i))  #类型都是<class 'lxml.etree._ElementUnicodeResult'>
    # if 'http://www.gov.cn/' not in i:
    #     print('http://www.gov.cn/' + i)
    # else:
    #     print(i)
    #改成三元运算表达式，完美解决
    # i2 = 'http://www.gov.cn/' + i if 'http://www.gov.cn/' not in i else i
    # print(type(i2))     #9条数据类型不一.......

# 网页连接的内容，正文
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
reque = requests.get('http://www.gov.cn/'+res[4],headers=header)
reque.encoding='utf-8'
z = reque.text


#有单独的p标记，也有p标记中含span的标记
htm = etree.HTML(z)
print(type(htm))        #初始化后，类型是<class 'lxml.etree._Element'>
re = htm.xpath("//td[@class='b12c']")   #是此处没有写对，尴尬了，9个不一样的。。。不能这么写
#string(.):获取当前节点所有字符串
# print(re[0].xpath('string(.)').strip())
# r=re.xpath('string(.)')
# print(type(r))类型都是<class 'lxml.etree._ElementUnicodeResult'>
# print(type(re))     #类型是list，并不一致，只能遍历处理了
for i in re:
    print(i.xpath('string(.)'))







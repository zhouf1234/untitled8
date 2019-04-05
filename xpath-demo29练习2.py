import requests
from lxml import etree

# 用xpath方法写
# 中华人民共和国 政策
# http: // www.gov.cn / zhengce /
# 最新政策标题的二级目录正文

#爬取主页面文件
def loadPage(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    c = request.text
    return c

#写正则找文件地址
def urll(c):
    # 取到所有网页的连接
    # http://www.gov.cn/zhengce/2018-11/29/content_5344537.htm
    # http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm,两种连接格式实际
    # 只取href后面的连接的话，无法连接，有些无前缀，需要进行拼接
    html = etree.HTML(c)
    res = html.xpath("//div[@class='list list_1']//ul//li//a/@href")
    # print(type(res))  #list类型
    for i in res:
        # print(type(i))  #类型都是<class 'lxml.etree._ElementUnicodeResult'>
        # 改成三元运算表达式，完美解决
        i2 = 'http://www.gov.cn/' + i if 'http://www.gov.cn/' not in i else i
        # 等同于此函数内loadpage2函数调用属性，在运行脚本时，不用写loadpage2了
        loadPage2(i2)


#写正则找分文件内容
def loadPage2(i2):
    #爬取网页连接的内容，正文
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(i2, headers=header)
    request.encoding = 'utf-8'
    z = request.text

    # 有单独的p标记，也有p标记中含span的标记
    htm = etree.HTML(z)
    re = htm.xpath("//td[@class='b12c']")
    # string(.):获取当前节点所有字符串
    # print(re[0].xpath('string(.)').strip())
    for i in re:
        # print(i.xpath('string(.)'))
        i3=i.xpath('string(.)')
        # print(i3)       #拼接的url后9个类型不一致，只显示了7个。。。。。。。。。。
        write_to_file(i3)

# 保存文件：怎么保存。。。。。。。
def write_to_file(i3):
    with open('xpath练习.txt','a',encoding='utf-8') as f:
        # 保存的有点难看，只保存到一个文件里面,只保存了7个
        f.write(i3)


#模拟main 函数，脚本就运行
if __name__=="__main__":
    url="http://www.gov.cn/zhengce/"
    c=loadPage(url)
    urll(c)
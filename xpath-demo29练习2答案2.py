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
    return c #返回主页面源码
    # print(c)
#写正则找文件地址
def urll(c):
    # 取到所有网页的连接
    # http://www.gov.cn/zhengce/2018-11/29/content_5344537.htm
    # http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm,两种连接格式实际
    # 只取href后面的连接的话，无法连接，有些无前缀，需要进行拼接
    html = etree.HTML(c)
    res = html.xpath("//div[@class='list list_1']//ul//li//a/@href")
    # print(res)  #list类型
    for i in res:
        j = 'http://www.gov.cn'
        s = i.find(j)
        if s == -1:
            i = j + i
        loadPage2(i)


#写正则找分文件内容
def loadPage2(i):
    # print(i2)
    #爬取网页连接的内容，正文
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(i, headers=header)
    request.encoding = 'utf-8'
    z = request.text
    # print(z)
    # # 有单独的p标记，也有p标记中含span的标记
    htm = etree.HTML(z)
    re = htm.xpath("//*[@id='UCAP-CONTENT']")
    # print(re)#匹配到了9个节点
    # string(.):获取当前节点所有字符串
    for i in re:
        # print(i)#td、div element类型
        i3=i.xpath('//p//text()')#查找文本
        for i4 in i3:
            # print(i4)#打印出文本内容
            write_to_file(i4)
# 保存文件：怎么保存。。。。。。。
def write_to_file(i4):
    with open('xpath练习2.txt','a',encoding='utf-8') as f:
        # 保存的有点难看，只保存到一个文件里面
        f.write('\n\t' + i4 + '\n\n')
        # print("正在下载" + filename + "文件")

#模拟main 函数，脚本就运行
if __name__=="__main__":
    url="http://www.gov.cn/zhengce/"
    c=loadPage(url)
    urll(c)
import re
import requests

# 新浪新闻
#https://news.sina.com.cn/china/
# 二级目录正文

#爬取主页面文件
def loadPage(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    s = request.text
    return s

#写正则找文件地址
def urll(s):
    # 正则取标题:第一次取到整个ul标签
    pat = re.compile('<ul.*?class="news-2".*?>(.*?)</ul>', re.S)
    new = re.findall(pat, s)
    print(type(new))
    for i in new:
        print(type(i))

    # 第二次取到第一次取到的ul标签的li标签的所有a标签的网页连接，字符类型必须一致
    patt1 = re.compile('<li><a.*?href="(.*?)".*?>.*?</a></li>', re.S)
    title = re.findall(patt1, i)
    print(type(title))
    for j in title:
        print(j)
        # 等同于此函数内loadpage2函数调用j属性，在运行脚本时，不用写loadpage2了
        loadPage2(j)


#写正则找分文件内容
def loadPage2(j):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    req = requests.get(j, headers=header)
    req.encoding = 'utf-8'
    z = req.text

    # 分析正文的正则
    z = re.sub('&nbsp;|<a.*?>|</a>', '', z)
    patt2 = re.compile('<p.*?>(.*?)</p>', re.S)
    w = re.findall(patt2, z)
    print(type(w))
    for h in w:
        print(h)

#保存文件：怎么保存。。。。。。。


#模拟main 函数，脚本就运行
if __name__=="__main__":
    url='https://news.sina.com.cn/china/'
    s=loadPage(url)
    urll(s)


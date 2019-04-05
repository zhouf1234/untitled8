import re
import requests

# 中华人民共和国 政策
# http: // www.gov.cn / zhengce /
# 最新政策标题二级目录所有正文

#爬取主页面文件
def loadPage(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    r = request.text
    return r

#写正则找文件地址
def urll(r):
    # 第一次取到整个div标签
    patt = re.compile('div.*?class="list list_1"(.*?)</div>', re.S)
    titles = re.findall(patt, r)
    # print(type(titles))
    for i in titles:
        print(type(i))
    # 第二次取到第一次取到的div标签的所有a标签的网页连接不相同的部分，字符类型必须一致
    # http://www.gov.cn/zhengce/2018-11/29/content_5344537.htm
    # http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm,两种连接格式实际
    patt1 = re.compile('<a.*?href=".*?zhengce\/(.*?content.*?)"\starget=.*?>.*?</a>', re.S)
    t = re.findall(patt1, i)
    # print(type(t))
    for j in t:
        # print(url+j)
        j = url+j
        # 等同于此函数内loadpage2函数调用j属性，在运行脚本时，不用写loadpage2了
        loadPage2(j)
    # for k in range(len(t)):
    #     print("[t%d]=%s" % (k, url+t[k]))
        #urllib.request.urlretrieve用于下载链接URL的内容到本地filepath里面
        #网页内容都找下来了。。。。但是我们需要的只是主体内容
        # urllib.request.urlretrieve(url+t[k], '%s.txt' % k)

#写正则找分文件内容
def loadPage2(j):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(j, headers=header)
    request.encoding = 'utf-8'
    r2 = request.text

    r2 = re.sub('<span.*?>|</span>|&nbsp;|<br>', '', r2)
    patt2 = re.compile('<p.*?>(.*?)</p>', re.S)
    w = re.findall(patt2, r2)
    print(type(w))
    for h in w:
        # 输出了所有检索的内容
        print(h)

#保存文件：怎么保存。。。。。。。


#模拟main 函数，脚本就运行
if __name__=="__main__":
    url="http://www.gov.cn/zhengce/"
    r=loadPage(url)
    urll(r)


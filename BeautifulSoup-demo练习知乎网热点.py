from bs4 import BeautifulSoup
import requests
import re

#爬取知乎网发现，今日热点的问题标题，回答者，回答。beautiful soup的方法尝试
# https://www.zhihu.com/explore

#分析主页面
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
req = requests.get('https://www.zhihu.com/explore',headers=header)
c = req.text
# print(type(c))

# 初始化解析
sou = BeautifulSoup(c,'lxml')

# 第一种方法
# 按属性值查找节点，查找到所有的div节点
di = sou.find_all(class_='explore-feed feed-item')
# print(di)
for d in di:
    for a in d.find_all(class_='question_link'):        #获取所有热点标题
        print(a.string)
    for ab in d.find_all(class_='author-link'):        #获取所有热点问题回答者
        print(ab.string)
    for tex in d.find_all(class_='content'):        #获取所有热点问题回答内容
        te = tex.string
        t = re.sub('<p>|</p>|<b>|</b>|</br>|<br>|<a.*?>|</a>|<figure>.*?</figure>|<li>|</li>|<i>|</i>|<ul>|</ul>|<blockquote>|</blockquote>|<span.*?>.*?</span>','',te)
        print(t)

    # 此方法保存的内容还是怪怪的
    # file = open('explore1.txt','a',encoding='utf-8')#打开文件 追加 编码格式
    # file.write('\n'.join([a.string,ab.string,t]))#join函数 连接字符串
    # file.write('\n' + '=' * 50 + '\n')#分割线
    # file.close()#关闭文件



# 第二种方法
# css选择器方法按属性值查找节点，查找到所有的节点
# di = sou.select('.explore-feed')
# # print(di)
# for d in di:
#     for a in d.select('.question_link'):         #获取所有热点标题
#         print(a.get_text())
#     for ab in d.select('.author-link'):         #获取所有热点问题回答者
#         print(ab.get_text())
#     # for tex in d.select('textarea'):              #获取所有热点问题回答内容,其中有很多标签符。。
#     #     print(tex.get_text())
#     for h in d.select('link'):           #通过找到分页面网址，去分页面取文本，没有乱七八糟的符号了
#         # print(h['href'])                #方法取href属性值，即分页面网址，下方取数据时拼接即可
#         header = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
#         re = requests.get('https://www.zhihu.com'+h['href'], headers=header)
#         c2 = re.text
#         # print(len(c2))
#         so = BeautifulSoup(c2, 'lxml')      #初始化分页面内容
#         spa = so.select('.RichText')        #解析，class属性找到节点列表
#         # print(spa)
#         for s in spa:
#             for p in s.select('p'):         #找到节点中的所有p节点
#                 print(p.get_text())         #获取p节点的所有内容，取分页面内容这段，同样适用第一种方法

        #  这样子怎么保存呢。。。。。。算了还是第一种吧





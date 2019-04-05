import requests
import re

#爬取知乎网发现，今日热点的问题标题，回答者，回答。解析方法不论
# https://www.zhihu.com/explore

#分析主页面
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
req = requests.get('https://www.zhihu.com/explore',headers=header)
c = req.text
# print(c)

#标题
# patt=re.compile('<div.*?class="explore-feed.*?".*?>.*?<a.*?class="question_link".*?>(.*?)</a>',re.S)
#回答者
# patt=re.compile('<div.*?data-author-name="(.*?)".*?>',re.S)
# 回答内容
# 方法一，直接主页面获取,可以先写替换正则，也可以后写,先写的似乎不太好用,a标签去不掉
# z = re.sub('&lt;|p&gt;|br&gt;|li&gt;|b&gt;|h2&gt|figure&gt.*?figure&gt;|blockquote&gt;|i&gt;|ul&gt;|hr&gt;','',c)
patt=re.compile('<div.*?class="zm-item-rich-text.*?">.*?<textarea hidden class="content">(.*?)</textarea>.*?</div>',re.S)
titles=re.findall(patt,c)
for i in titles:
    i2 = re.sub('&lt;|p&gt;|br&gt;|li&gt;|b&gt;|h2&gt;|/|figure&gt.*?figure&gt;|blockquote&gt;|a.*?&gt;|i&gt;|ul&gt;|hr&gt;','',i)
    print(i2)

# 方法二，分页面获取
# 1先获取分页面连接
# patt=re.compile('<div.*?data-entry-url="(.*?)">',re.S)
# titles=re.findall(patt,c)
# # 2再获取分页面内容
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# req = requests.get('https://www.zhihu.com'+titles[6],headers=header)
# req.encoding='utf-8'
# f = req.text
# # print(f)
# # # 3获取主页面内容
# zh = re.sub('<a.*?>|</a>|<span.*?>|</span>|<br>|<b>|</b>','',f)
# pa=re.compile('<p>(.*?)</p>',re.S)
# title=re.findall(pa,zh)
# # print(title)
# for i in title:
#     print(i)

# 标题，回答者，内容拼接
# 要求标题一行，回答者一行，内容一行，共三行的样式






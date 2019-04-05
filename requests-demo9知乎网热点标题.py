import requests
import re

#本次爬取的是知乎网的热点标题

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

#知乎网的发现页面的地址https://www.zhihu.com/explore
request = requests.get('http://www.zhihu.com/explore',headers=header)
patt=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles=re.findall(patt,request.text)
print(titles)

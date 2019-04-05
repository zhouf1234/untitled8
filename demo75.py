#代理池的获取，存储，检测
#用的demo74取得的可用代理ip地址爬取猫眼电影网首页榜单top100电影名等
import requests
import re

proxy = {
    "http":"47.104.193.87:8080",   #使用89网获取的这个可用ip地址
}
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('https://maoyan.com/board/4',headers=header,proxies=proxy)
m = request.text
patt = re.compile( '<a.*?title=.*?href=.*?data-act=.*?data-val=.*?>(.*?)</a>.*?<p.*?class="star">\s+(.*?)\s+</p>.*?<p.*?class="releasetime">(.*?)</p>', re.S)
titles = re.findall(patt, m)
for i in titles:
    print(i)
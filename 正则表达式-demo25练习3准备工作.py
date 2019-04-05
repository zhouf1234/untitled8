import requests
import re
# 中华人民共和国 政策
# http: // www.gov.cn / zhengce /
# 最新政策标题二级目录所有正文

# 分析主页面，准备工作：正则
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.gov.cn/zhengce/',headers=header)
request.encoding='utf-8'
c = request.text

# 第一次取到整个div标签
patt=re.compile('div.*?class="list list_1"(.*?)</div>',re.S)
titles=re.findall(patt,c)
print(type(titles))
for i in titles:
    print(type(i))
#第二次取到第一次取到的div标签的所有a标签的网页连接，字符类型必须一致
# http://www.gov.cn/zhengce/2018-11/29/content_5344537.htm
# http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm,两种连接格式实际
# 只取href后面的连接的话，无法连接，有些无前缀，需要进行拼接
patt1=re.compile('<a.*?href=".*?(zhengce.*?content.*?)"\starget=.*?>.*?</a>',re.S)
t=re.findall(patt1,i)
print(type(t))
for j in t:
    j='http://www.gov.cn/'+j
    print(j)

# 网页连接的内容，正文

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# reque = requests.get('http://www.gov.cn/zhengce/content/2018-12/06/content_5346276.htm',headers=header)
reque = requests.get('http://www.gov.cn/'+t[0],headers=header)
reque.encoding='utf-8'
z = reque.text


z = re.sub('<span.*?>|</span>|&nbsp;|<br>','',z)
patt2=re.compile('<p.*?>(.*?)</p>',re.S)
w=re.findall(patt2,z)
print(type(w))
for h in w:
    print(h)





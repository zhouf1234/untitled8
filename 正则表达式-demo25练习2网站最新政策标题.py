import requests
import re
# 中华人民共和国 政策
# http: // www.gov.cn / zhengce /
# 最新政策标题
# 二级目录
# 所有正文

# 分析页面
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.gov.cn/zhengce/',headers=header)
request.encoding='utf-8'
c = request.text
# print(c)
print(type(c))

# 第一次取到整个div标签
patt=re.compile('div.*?class="list list_1"(.*?)</div>',re.S)
titles=re.findall(patt,c)
print(type(titles))
for i in titles:
    print(type(i))
# print(type(i))
#第二次取到第一次取到的div标签的所有a标签的内容，字符类型必须一致
patt1=re.compile('<a.*?>(.*?)</a>',re.S)
t=re.findall(patt1,i)
# print(type(t))
for j in t:
    print(j)

# 保存,终于按序保存成文件了
file=open("./files/zuixin政策.txt","w+")
for i in range (len(t)):
    file.write(t[i]+"\n")
file.close()

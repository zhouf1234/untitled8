import re
content='http://www.baidu.com/serch/KERacn'

res = re .match('http.*?serch/(.*?)',content)   #非贪婪模式，KERacn没有匹配到
res1 = re .match('http.*?serch/(.*)',content)   #贪婪模式全部匹配到

print(res)
print(res.group(1))     #没有匹配到内容
print()

print(res1)
print(res1.group(1))    #匹配到了内容
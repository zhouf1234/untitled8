import pyquery
from pyquery import PyQuery as pq   #引入pyquery对象模块
import requests

html = '''
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0" active><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1" active><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html)  #将html当作参数，传递给pyquery类
print(doc('li'))    #传入li节点，选择所有li节点
print()

#解析url，指定一个url，初始化后，获取其title节点
#相当于用网页源代码，字符串的形式传给pyquery类来初始化
#这俩功能一样的，显示结果一样
do = pq(url='http://www.huawei.com/cn',encoding = 'utf-8')
print(do('title'))
d = pq(requests.get('http://www.huawei.com/cn').text)
print(d('title'))
print()

#解析一个txt文件，初始化后，获取其li节点
txt = pq(filename='02.txt')
print(txt('li'))
print()
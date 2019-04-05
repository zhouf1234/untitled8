from pyquery import PyQuery as pq

html = '''
<div class='warp'>
<div id='container'>
<ul class='list'>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
<a href="link6.html">six item</a>
</ul>
</div>
</div>
'''
#基本css选择器
doc = pq(html)
#先找id为container的节点，在选class为list的节点的li节点
#中间的空格代表下一节点，不空格
print(doc('#container .list li'))
print(type(doc('#container .list li')))     #类型为<class 'pyquery.pyquery.PyQuery'>
print()

#取class为list的节点
print(doc('.list'))
print()
#find方法取class为list的节点的所有子孙节点li
print(doc('.list').find('li'))
print()

print(doc('li').find('a'))
print()

#children()方法查找子节点
print(doc('.list').children())  #返回了所有class=list节点的子孙节点
print()
print(doc('.list').children('.item-0'))   #返回了class=list里的所有class=item-0的子节点
print()
print(doc('li').children())
print()

#parent()方法查找父节点所有内容
print(doc('.list').parent())    #返回了class=list节点的父节点所有内容
print()
#parents()方法
print(doc('.list').parents())   #没有给参数，此次打印了四次父节点内容。。，html一遍，body一遍，两个div两遍
print()
print(doc('.list').parents('div'))  #给了div参数就两遍
print()

#siblings兄弟节点
print(doc('.list .item-0.active').siblings())   #返回五个兄弟节点
print(doc('.list .item-0.active').siblings('.active'))  #返回一个兄弟节点，限定条件是active
print()

# 可以直接打印输出单个节点
print(doc('.item-0.active'))
print(type(doc('.item-0.active')))      #<class 'pyquery.pyquery.PyQuery'>
#单节点可以转化成字符串
print(str(doc('.item-0.active')))
print(type(str(doc('.item-0.active'))))     #<class 'str'>
print()

# items()多节点遍历输出
lis = doc('li').items()
print(type(lis))    #生成器类型<class 'generator'>
for li in lis:
    print(li,type(li))      #类型是 <class 'pyquery.pyquery.PyQuery'>
print()

# attr()获取属性值,两种方法，结果一致
print(doc('.item-0.active a').attr('href'))     #显示link3.html
print(doc('.item-0.active a').attr.href)         #显示link3.html
print()

# attr()获取属性值，调用多个节点的
print(doc('a'))     #所有a节点
print(doc('a').attr('href'))    #只会匹配到第一个href的属性值link2.html
print(doc('a').attr.href)       #只会匹配到第一个href的属性值link2.html
print()
#遍历获取每个a节点的href属性值
a = doc('a')
for i in a.items():
    print(i.attr.href)  #五个属性值都拿到了
print()

# text()获取文本:一个或多个
print(doc('.item-0.active a').text())   #显示：third item
print()
#html()获取节点内容
print(doc('.item-0.active').html())     #显示<a href="link3.html"><span class="bold">third item</span></a>
print()
print(doc('li').html())     #返回的是第一个节点的内容first item
print(doc('li').text())     #返回li节点的五个文本内容：first item second item third item fourth item fifth item
print(type(doc('li').text()))   #<class 'str'>类型
print(type(doc('li').html()))   #<class 'str'>类型
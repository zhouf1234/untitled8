from lxml import etree

# test.html的内容查看
'''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

# *：获取所有节点
# //：从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
# /：获取子节点
# .：获取当前节点
# ..：获取父节点
# @：获取属性

html = etree.parse('./test.html',etree.HTMLParser())
# *代表匹配所有节点，返回一个列表，每个元素都是Element类型，其后是节点名字
result = html.xpath('//*')
print(result)
print()

# 匹配所有节点li
resul = html.xpath('//li')
print(resul)
# print(resul[0])   #利用索引值取出其中一个对象
print()

# 匹配所有节点li的直接子节点a（查找子节点）
resu = html.xpath('//li/a')
print(resu)
print()

# 匹配ul的所有子孙节点a
res = html.xpath('//ul//a')
print(res)
print()

# href属性为link4.html的a节点，获取其父节点，再获取其class属性第一种方法
re = html.xpath("//a[@href='link4.html']/../@class")
print(re)       #['item-1']
#href属性为link4.html的a节点，获取其父节点，再获取其class属性第二种方法
re2 = html.xpath("//a[@href='link4.html']/parent::*/@class")
print(re2)      #['item-1']
print()

# 属性过滤：选取class=item-1的li节点
r = html.xpath("//li[@class='item-0']")
print(r)        #[<Element li at 0x1cb20845088>, <Element li at 0x1cb20845288>]
print()

#获取li节点的class='item-0的文本内容,三种方法
r1 = html.xpath("//li[@class='item-0']/text()")     #此处的含义是直接获取子节点
print(r1)        #item-0就显示['\r\n']，因为第二个li没有闭合
r2 = html.xpath("//li[@class='item-0']/a/text()")
print(r2)       #显示['first item', 'fifth item'] ，精确匹配
r3 = html.xpath("//li[@class='item-0']//text()")
print(r3)       #['first item', 'fifth item', '\r\n']，会参杂特殊符号
print()

# 获取li节点下a节点所有文本内容
s = html.xpath("//li/a/text()")
print(s)    #['first item', 'second item', 'third item', 'fourth item', 'fifth item']
print()

# 获取li节点下所有a节点的href属性，和属性过滤不同哦
s1 = html.xpath("//li/a/@href")
print(s1)   #['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
print()

s2 = html.xpath('//li/.')
print(s2)
print()
s3 = html.xpath('//li/..')
print(s3)



from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
#某些属性有多个节点，可以利用中括号索引的方法取到某个节点文本内容
#xpath有100多个函数，可以去www.w3school.com.cn/xpath/去查询使用
result = html.xpath('//li[1]/a/text()')
print(result)   #返回第一个节点，注意这里序号为1：显示['first item']
print()

#返回最后一个节点文本内容
resul = html.xpath('//li[last()]/a/text()')
print(resul)   #显示['fifth item']
print()

#取前面两个节点文本内容
resu = html.xpath('//li[position()<3]/a/text()')
print(resu)   #['first item', 'second item']
print()

#倒数第三个
resu = html.xpath('//li[last()-2]/a/text()')
print(resu)   #显示['third item']
print()

#li的祖先节点
res = html.xpath('//li[1]/ancestor::*')
print(res)

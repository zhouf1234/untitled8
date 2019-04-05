from lxml import etree

#https://blog.csdn.net/xiage/article/details/2620391运算符使用方法参照此链接

te = '''
<?xml version=”1.0”encoding=’ISO-8859-1”?>
<bookstore>
  <book>
<title lang=”eng”>Harry Potter<title>
<price>29.99</price>
<author>赵六</author>
  </book>
  <book>
<title lang=”eng”>Learning XML</title>
<price>39.95</price>
<author>张三</author>
</book>
<book>
   <title lang=”eng”>ORACLE”</title>
   <price>40.32</price>
   <author>Lary</author>
</book>
</bookstore>
'''
#0.选取bookstore元素中的book元素的所有title元素，且指定其中的price元素的值等于40.32
tes = etree.HTML(te)
title = tes.xpath('//book[contains(string(),"40.32")]/title/text()')
print(title)
print()

#1.选取bookstore元素中的book元素的所有title元素，且其中的price元素的值须大于35.0
title = tes.xpath('//book[price>35.0]/title/text()')
print(title)
print()
#2.选取属于bookstore元素的后代的所有book元素，而不管它们位于bookstore之下的什么位置
title = tes.xpath('//book//text()')
print(title)
print()

#4.选取所有带有属性的title元素
title = tes.xpath('//book/title[@*]/text()')
print(title)
print()
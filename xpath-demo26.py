import lxml
from lxml import etree

# text里的内容是当前文件夹下test.html的内容
text = '''
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
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
print()

# 也可以直接读取文本文件
htm = etree.parse('./test.html',etree.HTMLParser())
resul = etree.tostring(htm)
print(resul.decode('utf-8'))        #显示的是整个html的内容
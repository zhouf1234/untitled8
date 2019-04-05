from pyquery import PyQuery as pq

html = '''
<div class='wrap'>
    hello,world!
<p>this is a paragraph.</p>
</div>
'''

doc = pq(html)

# remove：删除节点
#remove：只输出hello world！
# print(doc('.wrap').text('hello,world!').text())
wrap = doc('.wrap')
wrap.find('p').remove()
print(wrap.text())







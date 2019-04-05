import requests#导入requests模块
from pyquery import PyQuery as pq #导入pyquery解析库

# 四种解析方法，这是pyquery的方法

url = 'http://www.zhihu.com/explore'#目标url

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}

html = requests.get(url,headers=headers).text#发送请求 响应网页内容
doc = pq(html)#初始化

items = doc('.explore-tab .feed-item').items()#找到目标节点 返回生成器
for item in items:
    question = item.find('h2').text()# 标题 h2节点下的文本内容
    author = item.find('.author-link-line').text()#回答者 span节点里a节点 文本
    answer = pq(item.find('.content').html()).text()#回答 textarea标签中 文本 先提取HTML文本 在用text（）提取纯文本
    file = open('explore.txt','a',encoding='utf-8')#打开文件 追加 编码格式
    file.write('\n'.join([question,author,answer]))#join函数 连接字符串
    file.write('\n' + '=' * 50 + '\n')#分割线
    file.close()#关闭文件

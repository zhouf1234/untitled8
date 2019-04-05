#代理服务器等

from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy = '127.0.0.1:53818'   #蓝灯获取的ip地址和端口
proxy_handler = ProxyHandler({
    'http':'http://'+proxy,
    'https':'https://'+proxy
})
opener = build_opener(proxy_handler)
try:
    res = opener.open('http://httpbin.org/get')
    print(res.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

# Prepared request  #数据结构

from requests import Request,Session

url = 'http://httpbin.org/post'

data = {
	'name':'germey'
}
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req) # 使用prepare_request 方法
r = s.send(prepped)#发送
print(r.text)
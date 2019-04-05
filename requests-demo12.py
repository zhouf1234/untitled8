import requests

#内置状态码对象查询
req = requests.get('http://www.baidu.com')
exit() if req.status_code == requests.codes.ok else print('请求超时。')
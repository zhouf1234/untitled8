import requests

#文件上传的测试

# 此次上传的是favicon这个图片
# files = {'file':open('favicon.ico','rb')}

# 此次上传的是01.txt这个记事本文件:不能写中文，此次显示乱码了
files = {'file':open('01.txt','rb')}

req = requests.post('http://httpbin.org/post',files=files)
print(req.text)
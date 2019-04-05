import requests

ip_ran = '127.0.0.1:53818'

url = 'http://httpbin.org/get'
proxy = {
        "http": ip_ran,
        "https": ip_ran,
    }
response = requests.get(url, proxies=proxy)
# print(response.text)
print(response.status_code) #获取网站动态响应码，200即为成功
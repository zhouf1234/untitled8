import requests
# 这里测试用到一个网站：http://icanhazip.com，这个网站会返回当前请求的ip地址，来测试代理ip是否配置成功。
# url = 'http://icanhazip.com'
url = 'http://httpbin.org/get'
# url = 'https://www.xicidaili.com/nt/1'
proxy = {
    "http":"119.101.114.198:9999",
}
response = requests.get(url,proxies=proxy)
print(response.text)

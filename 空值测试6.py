import requests
import re
import json
import random

# 这里测试用到一个网站：http://icanhazip.com，这个网站会返回当前请求的ip地址，来测试代理ip是否配置成功。
# url = 'http://icanhazip.com'
# proxy = {
#     "http":"47.104.193.87:8080",    #使用89网获取的这个可用ip地址去爬取猫眼电影网top100电影名等
# }
# # response = requests.get(url,proxies=proxy)
# # print(response.text)
#
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# request = requests.get('https://maoyan.com/board/4',headers=header,proxies=proxy)
# m = request.text
# patt = re.compile( '<a.*?title=.*?href=.*?data-act=.*?data-val=.*?>(.*?)</a>.*?<p.*?class="star">\s+(.*?)\s+</p>.*?<p.*?class="releasetime">(.*?)</p>', re.S)
# titles = re.findall(patt, m)
# for i in titles:
#     print(i)


#读取存放ip地址的json文件，随机一个ip地址和端口,以下一边测试ip是否可用，可用就爬取内容
ip_list = []
with open('hostip.json','r')as file:
    str2 = file.read()
    dat = json.loads(str2)
    for i in dat:
        i2 = i['host']+':'+i['port']    #结果如222.217.68.51:36539拼接为字符串
        # print(i2)
        ip_list.append(i2)
# print(ip_list)
ip_ran = random.choice(ip_list)  # 随机取ip地址
print(ip_ran)

proxy = {
        "http": ip_ran,
        "https": ip_ran,
    }
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

try:
    request = requests.get('https://maoyan.com/board/4',headers=header,proxies=proxy)
    m = request.text
    ip_code = request.status_code

    if ip_code == 200:
        print('该ip地址可用')    #如果可用就爬取内容
        patt = re.compile(
            '<a.*?title=.*?href=.*?data-act=.*?data-val=.*?>(.*?)</a>.*?<p.*?class="star">\s+(.*?)\s+</p>.*?<p.*?class="releasetime">(.*?)</p>',
            re.S)
        titles = re.findall(patt, m)
        for i in titles:
            print(i)
    else:
        print('不可用')

except Exception as error:  #异常捕获：Exception可以捕获所有的错误，不会使系统崩溃的
    print('该ip不可用！请删除')
    # 把错误信息提示反馈出来
    print(error)


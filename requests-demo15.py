import requests

#模拟获取cookie模拟登录后的页面信息：未成功。。。。。
header = {
    'Cookie':'_zap=4724130f-d10d-45d6-a7ac-d8c1e4dcc426; _xsrf=h0EPkW7bRz8ga5OOUXraEbQoAxMAUVGr; d_c0="APBi6q9Vnw6PTo04SYV6rXF-xjhHatPAz9M=|1543990940"; capsion_ticket="2|1:0|10:1543990943|14:capsion_ticket|44:NWRlMTYwOWM2ZGY2NDcxZmE1MWY3ZjE5YTcxZjVkYTI=|f70154980163c0b6ef347e6cacbc7723a27e7d17945cec4fcea7bfe639072530"; z_c0="2|1:0|10:1543990960|4:z_c0|92:Mi4xeUJ4bkRRQUFBQUFBOEdMcXIxV2ZEaVlBQUFCZ0FsVk5zTHowWEFDQk8xVWJaNS1sYkR5amJsOUU0SUZrRVFjU1J3|7f0b64d7b967a28c0500554ee046feaf5b6b743d5075eb7fefbcdb2d4e173f94"; q_c1=8b1f023435664d598d346176d1c4ee4f|1543990962000|1543990962000; __utma=51854390.283375248.1543990970.1543990970.1543990970.1; __utmc=51854390; __utmz=51854390.1543990970.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20181205=1^3=entry_date=20181205=1; tst=h; tgw_l7_route=c919f0a0115842464094a26115457122',
    'Host': 'www.zhihu.com',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

req = requests.get('http://www.zhihu.com/hot',headers=header)
req.encoding='utf-8'    #解决中文乱码
print(req.text)


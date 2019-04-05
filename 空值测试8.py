import requests
from lxml import etree
#已有账号模拟登陆
headers = {
    'Refer': 'https://github.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/68.0.3440.75 Safari/537.36',
    'Host': 'github.com'
}
login_url = 'https://github.com/login'      #登录网址
post_url = 'https://github.com/session'     #登录成功后的session的Request URL,f12的请求头里，post请求方式
logined_url = 'https://github.com/settings/profile' #登录成功后页面的网址

session = requests.session()    #定义一个变量，接收session对象
response = session.get(login_url, headers=headers)  # 访问GitHub的登录页面
selector = etree.HTML(response.text)
token = selector.xpath('//div//input[2]/@value')[0]  # 解析出登陆所需的authenticity_token信息
print(token)

post_data = {
            'commit': 'Sign in',
            'utf-8': '✓',
            'authenticity_token': token,
            'login': 'zhouf1234',
            'password': 'zhoufang000000'
        }
# 给session发送请求，POST表单提交，请求数据格式post_data；维持登录状态
respon = session.post(post_url, data=post_data, headers=headers)  #post_url是post的方法，所以用post
r = respon.text
response2 = session.get(logined_url, headers=headers)       #logined_url是get的方法，所以用get
r2 = response2.text

selector2 = etree.HTML(response2.text)  # 使用此方法提取用户名和账户图片连接，图片连接不登录无法打开，无法保存
img = selector2.xpath('//dl[@class="edit-profile-avatar mr-4 float-right"]//dd/img[1]/@src')
user = selector2.xpath('//dl[@class="edit-profile-avatar mr-4 float-right"]//dd/img[1]/@alt')
print(img, user)
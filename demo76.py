#模拟登陆
# 模拟Github登陆步骤：
#     1、请求头：self.headers，请求url；
#     4、authenticity_token获取；
#     2、设置session，保存登陆信息cookies
#     3、POST表单提交，请求数据格式post_data；
#     5、提取内容


import requests
from lxml import etree

class Login(object):
    def __init__(self):
        self.headers = {
            'Refer': 'https://github.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/68.0.3440.75 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()   # 此函数可以帮助我们维持一个会话，而且可以自动处理cookies，我们不用再去担心cookies的问题

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)  # 访问GitHub的登录页面
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')[0]   # 解析出登陆所需的authenticity_token信息
        # print(token)
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf-8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        # 给session发送请求，POST表单提交，请求数据格式post_data；维持登录状态；同登录后session的From Data查看
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)  #必须要写的，维持登录状态
        # if response.status_code == 200:
        #     # self.dynamics(response.text)
        #     print('ok')

        response = self.session.get(self.logined_url,headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def profile(self, html):  # 使用此方法提取个人的昵称和绑定的邮箱,用户名和账户图片连接，图片连接不登录无法打开。。
        selector = etree.HTML(html)
        # name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        # email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        img = selector.xpath('//dl[@class="edit-profile-avatar mr-4 float-right"]//dd/img[1]/@src')
        user = selector.xpath('//dl[@class="edit-profile-avatar mr-4 float-right"]//dd/img[1]/@alt')
        print(img,user)

if __name__ == "__main__":
    login = Login()
    login.login(email='1510880960@qq.com', password='zhoufang000000')  # 此处填自己的用户名和密码






import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains

from chaojiying import Chaojiying


def crack():
    # 保存网页截图
    browser.save_screenshot('222.png')

    # 获取 验证码确定按钮
    button = browser.find_element_by_xpath(xpath='//div[@class="geetest_panel"]/a/div')

    #  获取 验证码图片的 位置信息
    img1 = browser.find_element_by_xpath(xpath='//div[@class="geetest_widget"]')
    location = img1.location
    size = img1.size
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
        'width']
    print('图片的宽:', img1.size['width'])
    print(top, bottom, left, right)

    #  根据获取的验证码位置信息和网页图片  对验证码图片进行裁剪 保存
    img_1 = Image.open('222.png')
    capcha1 = img_1.crop((left, top, right, bottom - 54))
    capcha1.save('tu1-1.png')

    # 接入超级鹰 API 获取图片中的一些参数 (返回的是一个字典)
    cjy = Chaojiying('zhoufang', '000000', '898324')
    im = open('tu1-1.png', 'rb').read()
    content = cjy.PostPic(im, 9004)
    print(content)
    #  将图片中汉字的坐标位置 提取出来
    positions = content.get('pic_str').split('|')
    locations = [[int(number) for number in group.split(",")] for group in positions]
    print(positions)
    print(locations)

    #  根据获取的坐标信息 模仿鼠标点击验证码图片
    for location1 in locations:
        print(location1)
        ActionChains(browser).move_to_element_with_offset(img1, location1[0], location1[1]).click().perform()
        time.sleep(2)
    button.click()
    time.sleep(2)
    # 失败后重试
    lower = browser.find_element_by_xpath('//div[@class="geetest_table_box"]/div[2]').text
    print('判断', lower)
    if '验证成功' in lower:
        print('登录成功')
        time.sleep(3)
    # if lower != '验证失败 请按提示重新操作' and lower != None:
    #     print('登录成功')
    #     time.sleep(3)
    else:
        time.sleep(3)
        print('登录失败')
        # 登录失败后 , 调用 该函数 , 后台 则对该次判断不做扣分处理
        pic_id = content.get('pic_id')
        print('图片id为:', pic_id)
        cjy = Chaojiying('zhoufang', '000000', '898324')
        cjy.ReportError(pic_id)
        crack()


if __name__ == '__main__':
    browser = webdriver.Chrome()

    browser.get('https://www.jianshu.com/sign_in')
    browser.save_screenshot('login.png')

    # 填写from表单 点击登陆  获取验证码 的网页截图
    login = browser.find_element_by_id('sign-in-form-submit-btn')
    username = browser.find_element_by_id('session_email_or_mobile_number')
    password = browser.find_element_by_id('session_password')
    username.send_keys('15000667542')   #https://www.jianshu.com这个网址的登录手机号和密码
    time.sleep(1)
    password.send_keys('000000')
    time.sleep(3)
    login.click()
    time.sleep(6)
    crack()
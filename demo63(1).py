
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser .get('https://account.geetest.com/login')
input = browser.find_element_by_id('email')
input.send_keys('1347904922@qq.com')
time.sleep(2)
input2 = browser.find_element_by_id('password')
input2.send_keys('Zjk12345')
wait = WebDriverWait(browser, 10)  # 等待时间：10秒，id=content_left的节点出现
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
button.click()  #点击验证后，验证码图片出现
time.sleep(10)

img = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
time.sleep(2)
location = img.location
size = img.size
top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
print(top, bottom, left, right) #获取到验证码在网页中的具体位置
time.sleep(10)

screenshot = browser.get_screenshot_as_png()
screenshot = Image.open(BytesIO(screenshot))
captcha = screenshot.crop((left, top, right, bottom))
captcha.save('yan.png')     #依据获取的验证码位置，来保存验证码的网页截图
print('验证码图片已保存')
time.sleep(10)

slider = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
slider.click()       #拖动滑块
time.sleep(10)






#代理服务器，和demo65结果一致，方法不同，这个时chrome的方法，直接options这个pycham
from selenium import webdriver

proxy = '127.0.0.1:53818'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+proxy)
chorome = webdriver.Chrome(chrome_options = chrome_options)
chorome.get('http://httpbin.org/get')
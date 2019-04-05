from selenium import webdriver

# 执行js:此次知乎网热点下拉至底部，弹出alert弹框
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
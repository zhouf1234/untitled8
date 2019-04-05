# 三、实例  抓取猫眼电影排行
#
# 利用requests库和正则表达式 抓取猫眼电影TOP100 （requests比urllib使用更方便，由于没有学习HTML系统解析库 选用re）
# 1.目标 抓取电影名称 时间 评分 图片等
# url http://maoyan.com/board/4  结果以文件形式保存
# 2.分析
# offset 代表偏移量  如果为n 电影序号为n+1~n+10 每页显示10个
# 获取100 分开请求10次 offset 分别为0 10 20...90 利用正则提取相关信息
# 3.抓取页面
# ---------------------------------------------------------------------------------------------
# 分析页面
# 电影信息对应节点为<dd>
# 提取排名 class 为 board-index i节点内  正则   <dd>.*?board-index.*?>(.*?)</i>
# 电影图片 查看为第二个img链接 <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"
# 电影名字 p节点 class 为name  <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>
# 主演	 <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>
# 发布时间 <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>
# 评分 <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>
#
# 定义分析页面的方法 parse_one_page()
import requests #请求库
import re  #正则模块
import json #json模块
import time #时间模块
from requests.exceptions import RequestException
# 请求页面
def get_one_page(url):
    #异常处理
    try:
        header = {
            "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        }
        response = requests.get(url,headers=header)
        # 判断状态码是否为200
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

#解析页面
def parse_one_page(html):# html为网页源码
    #定义爬取规则
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )
    # 查找整个页面
    items = re.findall(pattern,html)
    # print(items)
    #遍历结果生成字典
    for item in items:
        yield {
            'index':item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else'',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip()+item[6].strip()
        }
        #返回一个生成器 yield

#写入文件
# 将提取结果 写入文件 通过json库 的dumps（） 实现字典的序列化 指定ensure_ascii 参数为 False
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        # ensure_ascii=False 保证输出结果为中文
        f.write(json.dumps(content,ensure_ascii=False)+'\n')


# 定义一个main函数 调用get_one_page 发送请求 参数offset 网页偏移量# 调用get_one_page 分页爬取 打印结果
def main(offset):
    #拼接url地址
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    # 请求函数
    html = get_one_page(url)
    # print(html)
    # 解析函数 和 文件保存函数
    for item in parse_one_page(html):#遍历生成器
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset = i *10)
        #延时处理
        time.sleep(3)

# 最基础的实例 做好总结
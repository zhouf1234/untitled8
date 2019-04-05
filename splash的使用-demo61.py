import requests
from urllib.parse import quote

# splash在pycham里用，此次lua的字符串即是splash的运行脚本语句

# 用urllib.parse模块里的 quote()方法将脚本进行URL转码，
# 随后构造了Splash请求URL，将其作为lua_source参数传递，这样运行结果就会显示Lua脚本执行后的结果
# Lua脚本均可以用此方式与Python进行对接，
# 所有网页的动态渲染、模拟点击、表单提交、页面滑动、延时等待后的一些结果均可以自由控制

# splash接口还支持代理设置、图片加载设置、Headers设置、请求方法设置，
# 具体的更多用法可以参见官方文档https://splash.readthedocs.io/en/stable/api.html#render-html

# 通过lua_source参数传递了转码后的Lua脚本，通过execute接口获取了最终脚本的执行结果
# execute接口可实现与Lua脚本的对接
lua = '''
function main(splash)
    return 'hello'
end
'''

url = 'http://192.168.99.100:8050/execute?lua_source='+quote(lua)
res = requests.get(url)
# print(res.text)         #输出hello


lua2 = '''
function main(splash)
    local treat = require('treat')
    local response = splash:http_get('http://httpbin.org/get')
    return {
    html = treat.as_string(response.body),
    url = response.url,
    status = response.status
    }
end
'''

url2 = 'http://192.168.99.100:8050/execute?lua_source='+quote(lua2)
res2 = requests.get(url2)
print(res2.text)    #返回结果是JSON形式，我们成功获取了请求的URL、状态码和网页源代码
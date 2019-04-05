
# proxies 参数

import requests

#代理设置，此处的eeee,aaaaa瞎写的，实际
# proxies = {
#     'http':'http:127.0.0.1:eeee',
#     'https':'http:127.0.0.1:aaaaa'
# }
#
# requests.get('http://www.baidu.com',proxies=proxies)


# 如果是 HTTP basic Auth（客户端之前没有认证过，需要输入用户名和密码认证后才可以访问）
# 示例：
#代理设置第二种
proxies = {
    'http':'http//user:password@127.0.0.1:12345'
}
requests.get('http://www.baidu.com',proxies=proxies)

# SOCKS协议（网络传输协议，主要用于客户端与外网服务器之间通讯的中间传递）
# 需要先安装socks库（pip install -U requests[socks]）

proxies = {
    'http':'socks5://user:password@host:port',
    'https':'socks5://user:password@host:port'
}

requests.get('http://www.baidu.com',proxies=proxies)
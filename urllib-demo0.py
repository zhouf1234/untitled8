#请求方式：get。请求地址host，遵循的网络协议http/1.1，版本号
# GET https://www.baidu.com/img/bd_logo1.png HTTP/1.1
# Host: www.baidu.com
# Connection: keep-alive
# Pragma: no-cache
# Cache-Control: no-cache
#
# #header:添加信息
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
# Accept: image/webp,image/apng,image/*,*/*;q=0.8
# Referer: https://www.baidu.com/
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
#
# #cookie
# Cookie: BAIDUID=C9D5F1E249B6A784F80F896F4C809766:FG=1; BIDUPSID=C9D5F1E249B6A784F80F896F4C809766; PSTM=1533196810; delPer=0; BD_UPN=12314753; BDRCVFR[ZQuaEB4a2uC]=mk3SLVN4HKm; delPer=0; BD_HOME=0; H_PS_PSSID=26522_1450_27212_21096_27244_27509; BDSVRTM=0
#

import urllib.request
# import request
res=urllib.request.urlopen('http://www.baidu.com')
print(res.read())
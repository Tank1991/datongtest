import requests
import re
from urllib.parse import parse_qsl
# 1.先访问首页
url1 = "http://zzk-s.cnblogs.com/s/blogpost"

r1 = requests.get(url1, allow_redirects=False, verify=False)
# 第2种情况，cookie在重定向页面内容里
print(r1.status_code)
print(r1.headers)
print(r1.cookies)

# # 获取cookies
# c = r1.headers
# print(c["Set-Cookie"])
#
# # cookies放请求头部
# h = {"Cookie": c["Set-Cookie"]}
#
# par = {
#     "Keywords": "yoyo"
#        }
# r2 = requests.get(url1,headers=h, params=par)
# print(r2.text)

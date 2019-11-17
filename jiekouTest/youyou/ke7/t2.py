import requests
import re
from urllib.parse import parse_qsl
# 1.先访问首页
url1 = "http://zzk-s.cnblogs.com/s/blogpost"

r1 = requests.get(url1, allow_redirects=False, verify=False)
# 第2种情况，cookie在重定向页面内容里
print(r1.status_code)
print(r1.text)

# # 正则提取：知道前后取中间，遇到字符加转义
# c = re.findall("blogpost\?(.+?)\">", r1.text)
# print(c[0])
# cook = dict(parse_qsl(c[0]))
# print(cook)
#
# # cookies传入
# par = {
#     "Keywords": "yoyo"
#        }
# r2 = requests.get(url1, cookies=cook, params=par)
# print(r2.text)
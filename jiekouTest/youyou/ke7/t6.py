# coding:utf-8
import requests
import re
url = "http://zzk-s.cnblogs.com/s/blogpost"
# 禁止重定向请求 allow_redirects=False
r1 = requests.get(url,allow_redirects=False)
print(r1.status_code)

# 正则获取返回body内容的cookie信息
r = r1.text
print(r)

# 知道前后取中间
c = re.findall("blogpost\?(.+?)\"", r)
print(c[0])  # 返回的是list



# print(r1.headers)  # 返回的头部信息
#
# c = r1.headers['Set-Cookie']
# print(c)
#
# h = {
#     "Cookie": c
#     }
# r2 = requests.get(url, headers=h)
# print(r2.text)


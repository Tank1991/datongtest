# coding:utf-8

import requests

url = "http://zzk-s.cnblogs.com/s/blogpost?Keywords=yoyo"
# h = {
#     "Cookie": "AspxAutoDetectCookieSupport=1"
#     }

r = requests.get(url)

print(r.url)
print(r.status_code)
print(r.headers)
print(r.text)
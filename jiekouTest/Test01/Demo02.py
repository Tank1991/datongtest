# coding:utf-8

import  requests

url = "https://zzk-s.cnblogs.com/s/blogpost?Keywords=youyou"
h = {
    "Cookie":"AspxAutoDetectCookieSupport=1"
}
r = requests.get(url,verify=False ,headers = h)


print(r.status_code)
print(r.headers)
print(r.text)






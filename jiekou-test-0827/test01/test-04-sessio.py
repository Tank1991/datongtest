# coding:utf-8
import requests

# 忽略警告
import urllib3
urllib3.disable_warnings()

s = requests.session()
url = ""

#加cookies
# c = {
#     "key1" : "value1",
#     "keey2" : "value2"
# }

c = requests.cookies.RequestsCookieJar()
c.set("key1" , "value1")
c.set("keey2" , "value2")
s.cookies.update(c)

r1 = s.post(url)











# coding:utf-8
import requests
import re
# 禅道登录案例

url = "http://127.0.0.1/zentao/user-login.html"

h ={
    "Content-Type": "application/x-www-form-urlencoded"
   }
body = {
    "account": "admin",
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "referer": "http://127.0.0.1/zentao/my/",
    "keepLogin[]": "on"
      }

r = requests.post(url, headers=h, data=body) # url, headers=h, data=body
print(r.status_code)
# print(r.text)  # 如果。text出现乱码
a = r.content.decode("utf-8")
print(a)

# 获取登录的cookies
cook = r.cookies
print(cook)    # Jar的格式

c = dict(cook)  # dict
print(c)

# 访问登录之后的请求
url2 = "http://127.0.0.1/zentao/my/"
r2 = requests.get(url2, cookies=c)
print(r2.content.decode("utf-8"))



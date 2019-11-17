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
print(r.cookies)  # RequestsCookieJar

# 获取登陆后的cookies传给下个登陆后的请求
cook = dict(r.cookies)
print(cook)




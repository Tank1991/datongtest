#coding:utf-8

import  requests
import  re
import urllib3
urllib3.disable_warnings()
#禅道的登录案列
url = "http://127.0.0.1:81/zentao/user-login.html"
par = {

    }

h = {
    "Content-Type": "application/x-www-form-urlencoded"
    }

body = {
    "account": "admin",
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "keepLogin[]": "on",
    "referer": "http://127.0.0.1:81/zentao/my/"
    }
r = requests.post(url,data = body,headers =h) #data = body  data是对于不是json的格式

print(r.status_code)
# print(r.text)
res = r.content.decode("utf-8")
print(res)

#获取登陆之后的cookies
cook = r.cookies
print("---------")
print(cook)
cook = dict(cook)
print("字典格式--------------")
print(cook)

#禅道登录之后的请求

url2 = "http://127.0.0.1:81/zentao/my/"
r2 = requests.get(url2,cookies= cook)

print(r2.content.decode("utf-8"))



























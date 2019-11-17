#coding:utf-8
import requests
import  re
import urllib3
urllib3.disable_warnings()

#python 里面的微型浏览器，无界面
s = requests.session()
print("打开浏览器的时候，没有cookies===="+str(s.cookies))

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
r = s.post(url,data = body,headers =h) #data = body  data是对于不是json的格式

print(r.status_code)
# print(r.text)
result = r.content.decode("utf-8")
print(result)
print("打开浏览器后，cookies===="+str(s.cookies))
#访问登陆之后的请求

url2 = "http://127.0.0.1:81/zentao/my/"
r2 = s.get(url2)
# print(r2.content.decode("utf-8"))







































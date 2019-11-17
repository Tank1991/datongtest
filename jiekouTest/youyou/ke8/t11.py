# coding:utf-8
import requests

# python里面的微型浏览器，无界面
s = requests.session()

# 首先打开浏览器时候，无cookis
print(s.cookies)  # Jar[]

# 禅道登录案例
url = "http://127.0.0.1/zentao/user-login.html"
h = {
    "Content-Type": "application/x-www-form-urlencoded"
   }
body = {
    "account": "admin",
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "referer": "http://127.0.0.1/zentao/my/",
    "keepLogin[]": "on"
      }

r = s.post(url, headers=h, data=body)  # url, headers=h, data=body
print(r.status_code)
# print(r.text)  # 如果。text出现乱码
a = r.content.decode("utf-8")
print(a)
# 登录完之后的cookies

print(s.cookies)  # CookieJar[<Cookie

# 访问登录之后的请求
url2 = "http://127.0.0.1/zentao/my/"
r2 = s.get(url2)
# print(r2.content.decode("utf-8"))

print(s.cookies)






# coding:utf-8
import requests
import re
# 禅道登录案例

url = "http://127.0.0.1/zentao/user-login.html"

h ={
    "Content-Type": "application/x-www-form-urlencoded"
   }
body = {
    "account": "admin1",
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "referer": "http://127.0.0.1/zentao/my/",
    "keepLogin[]": "on"
      }

r = requests.post(url, headers=h, data=body) # url, headers=h, data=body
print(r.status_code)
# print(r.text)  # 如果。text出现乱码
a = r.content.decode("utf-8")
print(a)


# try:
#     # 正则提取  只要是文本都可以提取
#     # 默读三遍：知道前后取中间，遇到字符加转义
#     result = re.findall("body\{(.+?)\}", a)
#     print(result[0])
# except:
#     print("登录ok")






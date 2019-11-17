#coding:utf-8

import  requests
import  re
#禅道的登录案列
url = "http://127.0.0.1:81/zentao/user-login.html"
par = {

    }

h = {
    "Content-Type": "application/x-www-form-urlencoded"
    }

body = {
    "account": "admin1",
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "keepLogin[]": "on",
    "referer": "http://127.0.0.1:81/zentao/my/"
    }
r = requests.post(url,data = body,headers =h) #data = body  data是对于不是json的格式

print(r.status_code)
# print(r.text)
res = r.content.decode("utf-8")
print(res)

#正则表达提取
result = re.findall("alert\(\'(.+?)\'\)",res )
print(result[0])
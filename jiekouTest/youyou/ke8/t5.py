# coding:utf-8
import requests

url = "http://zzk-s.cnblogs.com/s/blogpost"
r1 = requests.get(url)
print(r1.status_code)
u2 = r1.url   # 获取返回的url地址

# 获取返回的cookies
cook = u2.split("?")[1]
print(cook)

# 字典格式的cookie
ccc = cook.split("=")  # list
c = {}   # 定义空字典
c[ccc[0]] = ccc[1]
print(c)
# AspxAutoDetectCookieSupport=1&nnn=2
h = {
    "Cookie": cook
     }

# 第一种可以把cookies放头部，格式 name=value;name2=value2
r2 = requests.get(url, headers=h)  # cookies=c
print(r2.status_code)
print(r2.text)

# c = {
#     "name1": "value1",
#     "name2": "value2",
#     "name3": "value3",
# }

# 第二种可以把cookies单独拿出来传，字典格式
r3 = requests.get(url, cookies=c)  # cookies=c
print(r3.status_code)
print(r3.text)


#coding:utf-8

from urllib.parse import parse_qsl
import  requests
import urllib3
urllib3.disable_warnings()
url = "http://zzk-s.cnblogs.com/s/blogpost"

r = requests.get(url,verify = False)

print(r.status_code)
print(r.url)   #访问过后的url
result = r.urls

#获取返回的cookies
cook = result.split("?")[1]
print(cook)

ccc = cook.split("=")

#字典格式的cookies
c = {}
c[ccc[0]] = ccc[1]
print(c)

h = {
    "Cookie": cook
    }

#第一种可以把cookies
r2 = requests.get(url,headers=h)   #headers=h
print(r2.status_code)
print(r2.text)


#第二种可以把cookies单独拿出来传，字典格式
r3 = requests.get(url,cookies=c)   #cookies=c
print(r3.status_code)
print(r3.text)









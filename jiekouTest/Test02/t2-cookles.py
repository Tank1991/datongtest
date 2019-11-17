#coding:utf-8
import requests


url = "https://zzk-s.cnblogs.com/s/blogpost"

r = requests.get(url,allow_redirects=False)  #allow_redirects=False

print(r.status_code)
print(r.headers)

cook = r.headers["Set-Cookie"]
print(cook)

h ={
    "Cookie":cook
    }

r1 = requests.get(url,headers=h)
print(r1.text)



























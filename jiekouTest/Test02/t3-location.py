#coding:utf-8
import requests
import urllib3
urllib3.disable_warnings()
url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

r = requests.get(url,verify=False)

print(r.history)
print(r.status_code)
print(r.url)


r1 = r.history[0]
print(r1.status_code)
print(r1.url)
print(r1.headers)
print("*****************************")
print(r1.text)



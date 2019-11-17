# coding:utf-8
import requests
import urllib3
urllib3.disable_warnings()
url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

r = requests.get(url, verify=False)
print(r.history)  # 多个返回的对象
print(r.status_code)
print(r.url)

# 获取其中一个
r1 = r.history[0]  # 第一个返回对象
print(r1.status_code)
print(r1.headers)
print(r1.text)

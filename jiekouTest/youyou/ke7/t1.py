import requests
from urllib.parse import parse_qsl
# 1.先访问首页
url1 = "http://zzk-s.cnblogs.com/s/blogpost"

r1 = requests.get(url1, verify=False)
# 第1种情况，cookie在重定向后的url上
res_url = r1.url
print(res_url)   # 重定向后cookie在url的头部了

canshu = res_url.split("?")[1]  # 获取问号后面的参数
# 获取cookies,转字典
cook = dict(parse_qsl(canshu))
print(cook)  # 结果 {'AspxAutoDetectCookieSupport': '1'}


# cookies传入
par = {
    "Keywords": "yoyo"
       }
r2 = requests.get(url1, cookies=cook, params=par)
print(r2.text)





# url = "http://zzk-s.cnblogs.com/s/blogpost?Keywords=yoyo"
# # h = {
# #     "Cookie": "AspxAutoDetectCookieSupport=1"
# #     }
#
# r = requests.get(url)
#
# print(r.url)
# print(r.status_code)
# print(r.headers)
# print(r.text)
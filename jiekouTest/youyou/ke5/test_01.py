# coding:utf-8
import requests


# url = "http://japi.juhe.cn/qqevaluate/qq?key=8dbee1fcd8627fb6699bce7b986adc45&qq=283340479"
# r = requests.get(url)

url = "http://japi.juhe.cn/qqevaluate/qq"
# 参数：key=8dbee1fcd8627fb6699bce7b986adc45&qq=283340479
par = {
    "key": "8dbee1fcd8627fb6699bce7b986adc45",
    "qq": "283340479"
     }

r = requests.post(url, params=par)  # url, params=par

print(r.status_code)       # 1.状态吗
print(r.headers)           # 2.返回的头部  字典是无序的
print(r.text)              # 3.返回的正文


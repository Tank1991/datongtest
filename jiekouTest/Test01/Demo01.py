# coding:utf-8
import requests

# url = "http://japi.juhe.cn/qqevaluate/qq?key=8dbee1fcd8627fb6699bce7b986adc45&qq=289918161"
url = "http://japi.juhe.cn/qqevaluate/qq"

par = {
    "key":"8dbee1fcd8627fb6699bce7b986adc45",
    "qq":"1173540745"
}

# r = requests.get(url,params=par)
r = requests.post(url,params=par)

print(r.status_code)
print(r.headers)
print("Set-Cookie :"+ r.headers["Set-Cookie"])
if  "gzip" in r.headers['Content-Type']:
    print("这是gzip的返回格式 "+r.content)
    print("返回的格式是："+r.headers['Content-Type'])
else:
    print("这不是gzip的返回类型 "+r.text)
    print("返回的格式是："+r.headers['Content-Type'])

# print(r.text)








# key = 8dbee1fcd8627fb6699bce7b986adc45









































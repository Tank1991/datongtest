# coding:utf-8
import requests
import json
url = "http://japi.juhe.cn/qqevaluate/qq"

# 这个key参数是我个人申请的，所以本群内部使用就行了，希望大家别乱发
par = {
      "key": "8dbee1fcd8627fb6699bce7b986adc45",  # appkey需要注册申请
      "qq":  "283340479"
       }
r = requests.get(url, params=par)
# r111 = r.text # 打印文本
# print(type(r111))
# print(r111)
#
# print(eval(r111))
# print(json.loads(r111))


r222 = r.json()  #  requests自带json解析器
print(type(r222))
print(r222) # 这个本来就字典
print(r222['reason'])

# 一层层取值
print(r222['result']['data']['analysis'])


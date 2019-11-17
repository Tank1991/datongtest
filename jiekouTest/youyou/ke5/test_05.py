# coding:utf-8
import requests
url = "https://smc.api.xxx.com/Account/SmcLogin"
par = {
    "a": "xxx"
    }
h ={
    "Content-Type": "application/json",
    "Cookie": "xxxxxxxxx"
    }
# 在python 里面body写成字典
body = {"RequestStamp": "stamp-1525484256872",
        "Callback": "110",
        "PostTime": 1525484256111,
        "PostContent": {"UserName": "000000",
                          "Password": "c831b04de153469d",
                          "PassCode": ""},

        "qita": ""
        }

usrname = body["PostContent"]["UserName"]
print(usrname)

# 发json格式post
r = requests.post(url, headers=h, json=body, params=par)  # url, json=body ,headers=h


# coding:utf-8
import requests

# 忽略警告
import urllib3
urllib3.disable_warnings()

# 第一种 json
url = ""
par = {
    #传的是url 后面问号传值的数据
}
h = {
    #这是请求的头信息
}
body = {
    "key1" : "value1"
}
r = requests.get(url,json= body,headers = h, params= par, verify= False)   # json= body,headers = h,    # verify= False  忽略警告

# 第二种 x-www-form-urlencoded    (禅道登录)
url = ""
par = {
    #传的是url 后面问号传值的数据
}
h = {
    #这是请求的头信息
}
body = {
    "key1" : "value1"
}
r = requests.get(url , data = body , headers = h, params = par, verify =  False)   # data= body,headers = h,    # verify= False  忽略警告


# 第三种 multipart/from-data  （文件上传）
# 第四种 octets/stream   (文件下载)



url = "http://v.juhe.cn/weather/index"

par = {
    "format" :  "2",
    "cityname" : "苏州",
    "key": "aa647f8c1d863b9cd008b9a5bc56f815"
}
r = requests.get(url,params= par, verify= False)       # verify= False  忽略警告


print(r.text)
res = r.content.decode("utf-8")    #不会出现乱码的情况

#正则表达式         一前一后，特殊转义\
import re
result = re.findall("前面的.\(\.+?\)\.后面的",res)
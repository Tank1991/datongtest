# coding:utf-8
import requests

# 第一种是在url后面问号传值的    r = requests.get(url)
# 第二种是  r = requests.get(url,params= par) 加上传的值

url = "http://v.juhe.cn/weather/index?format=2&cityname=%E8%8B%8F%E5%B7%9E&key=aa647f8c1d863b9cd008b9a5bc56f815"

par = {
    "format" :  "2",
    "cityname" : "苏州",
    "key": "aa647f8c1d863b9cd008b9a5bc56f815"
}
r = requests.get(url,params= par)


# 有gzip压缩的时候，不能用text
print(r.text)

# 字节响应的时候，自动解压gzip
print(r.content)









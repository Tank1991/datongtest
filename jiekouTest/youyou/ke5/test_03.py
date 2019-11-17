# coding:utf-8
import requests

r = requests.get("https://www.baidu.com")
# print(r.text)  # 有gzip压缩这种，就不能.text

# print(r.content)  # 字节方式响应，自动解压gzip
print(r.url)  # 如果有重定向时候，返回的就是最后一个地址
print(r.cookies)


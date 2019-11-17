#coding:utf-8

import  requests

url = "https://www.baidu.com/"


r = requests.get(url,verify=False)


# print(r.text)    #有gzip压缩的时候，就不能 .text
print(r.content)    #字节方式响应， 自动解码 gzip
print(r.url)

print(r.cookies)
print(r.encoding)
print(r.raise_for_status())




# coding:utf-8
import requests

# 作者：上海-悠悠 QQ交流群：588402570
url = "http://httpbin.org/post"

# python3字符串换行，在右边加个反斜杠
# body = '<?xml version="1.0" encoding = "UTF-8"?>' \
#        '<COM>' \
#        '<REQ name="上海-悠悠">' \
#        '<USER_ID>yoyoketang</USER_ID>' \
#        '<COMMODITY_ID>123456</COMMODITY_ID>' \
#        '<SESSION_ID>absbnmasbnfmasbm1213</SESSION_ID>' \
#        '</REQ>' \
#        '</COM>'

fp = open("data", encoding="utf-8")

# 遇到编码报错时候，对body进行encode
r = requests.post(url, data=fp.read().encode("utf-8"))
print(r.text)
fp.close()
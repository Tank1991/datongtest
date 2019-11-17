# coding:utf-8
import requests

# 忽略警告
import urllib3
urllib3.disable_warnings()

#禁止重定向
# allow_redirects = False

# 第一种   在返回的url上
# 头部和cook可以选择一个
url = ""

h = {
    "Cookie" : ""
}

cook = {
    "key"  : "value",
    "key2" : "value2"
    }

r = requests.get(url , headers = h ,  cookies = cook)

# 第二种   藏在返回的内容里面
#  用正则公式去取值


# 第三种   在返回的头部

# 可以先获取接口的返回头部信息，再一层一级去取值   键值对

# 登录后cookies关联
# 如果cookies再返回的头部，可以用r.cookies来获取     此时cookies是jar包的形式

cook = r.cookies    #获取返回头部的cookies
c = dict(cook)     #字典形式







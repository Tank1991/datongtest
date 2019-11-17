#coding:utf-8
import requests
import re

s = requests.session()
print(s.cookies)

url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

# 往s里面更新cookies, 绕过验证码登录
c = requests.cookies.RequestsCookieJar()  # jar包
c.set(".CNBlogsCookie", "自己抓包" )
c.set(".Cnblogs.AspNetCore.Cookies", "自己抓包")
s.cookies.update(c)


#看是不是更新过去了
print(s.cookies)

r = s.get(url,verify=False)
print(r.text)






















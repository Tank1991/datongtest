# coding:utf-8
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

# 看是不是更新过去了
print(s.cookies)

r1 = s.get(url, verify=False)
print(r1.text)

# 登陆成功之后，保存一个草稿箱
body = {
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"FE27D343",
    "Editor$Edit$txbTitle":"20180710 测试草稿箱",
    "Editor$Edit$EditorBody":"20180710 测试草稿箱20180713 测试草稿箱",
    "Editor$Edit$Advanced$ckbPublished":"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on",
    "Editor$Edit$Advanced$chkComments":"on",
    "Editor$Edit$Advanced$chkMainSyndication":"on",
    "Editor$Edit$Advanced$txbEntryName":"",
    "Editor$Edit$Advanced$txbExcerpt":"",
    "Editor$Edit$Advanced$txbTag":"",
    "Editor$Edit$Advanced$tbEnryPassword":"",
    "Editor$Edit$lkbDraft":"存为草稿"
    }
r2 = s.post(url,data=body)
print(r2.text)

u = r2.url
print(u)

postid = re.findall("postid=(.+?)&", r2.url)
print(postid[0])


# 删除接口
url3 = "https://i.cnblogs.com/post/delete"
body = {
    "postId": postid[0]
      }
r3 = s.post(url3, json=body, verify=False)
print(r3.text)









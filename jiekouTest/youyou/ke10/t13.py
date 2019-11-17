# coding:utf-8
import requests
import re
import requests
from selenium import webdriver
import re
import time
import urllib3
urllib3.disable_warnings()

'''
抽象思路： 写四个函数
1. 登录
2. 保存草稿
3. 获取postid
4. 删除
'''

# s = requests.session()

def login(s):
    # 往s里面更新cookies, 绕过验证码登录
    c = requests.cookies.RequestsCookieJar()  # jar包
    c.set(".CNBlogsCookie", "9A9A9767628321FDDD1521002C2E0A38D912B6DF436B1C43CAE99790D4ED4598E2198DD249BDE472F0D91B65DF954A8F205919F6E7609720A7DC3838C9419B37BB41305C2AFB7FFA3C77E879AC638BB4C42BD9B1" )
    c.set(".Cnblogs.AspNetCore.Cookies", "CfDJ8FHXRRtkJWRFtU30nh_M9mD-9nTu9zUNwnJoeK1GjMRJXGOi_YGGwFBhFTYaHcYFHl8ZxDRSDzSWLVx98mfYxU1JvByntmvfhRKFq4ZdYHcC7QftD4SFxP60KfSTMyRk9ynpLRblOTItifIF_MdGLJzXGPNkzn8XN-11eFUFiCnb__99Lf3WYeuIPj_hqVJ_reviYZRSX2VtQNO78imwQ0nuS8v5P2avHkybBnE0Azp9YfLUf45dL9TAtxL2el7h71s5ZKfYBi0I86Qp3DjFDgO-dONs3htsVaSy7Twb1FNTvgbJKKHJRlkMBQQ49m8oVg")
    s.cookies.update(c)

    # 看是不是更新过去了
    # print(s.cookies)

    # r1 = s.get(url, verify=False)
    # print(r1.text)

def saveBlog(s, title, tail):
    # 登陆成功之后，保存一个草稿箱

    # title = "20180709 测试草稿箱"
    # tail = "20180709 测试草稿箱20180713 测试草稿箱"

    url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    body = {
        "__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "FE27D343",
        "Editor$Edit$txbTitle": title,
        "Editor$Edit$EditorBody": tail,
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$Advanced$chkDisplayHomePage": "on",
        "Editor$Edit$Advanced$chkComments": "on",
        "Editor$Edit$Advanced$chkMainSyndication": "on",
        "Editor$Edit$Advanced$txbEntryName":"",
        "Editor$Edit$Advanced$txbExcerpt":"",
        "Editor$Edit$Advanced$txbTag":"",
        "Editor$Edit$Advanced$tbEnryPassword":"",
        "Editor$Edit$lkbDraft":"存为草稿"
        }
    r2 = s.post(url,data=body, verify=False)
    print(r2.url)
    return r2.url

def getPostid(url):
    postid = re.findall("postid=(.+?)&", url)
    print(postid[0])
    return postid[0]

def deleteBlog(s, postid):
    # 删除接口
    url3 = "https://i.cnblogs.com/post/delete"
    body = {
        "postId": postid
          }
    r3 = s.post(url3, json=body, verify=False)
    print(r3.text)

if __name__ == "__main__":
    # if 下面是当前脚本调试语句，相当于自测内容
    s = requests.session()
    login(s)
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    print(timestamp)

    title = "自己写一个title %s"%timestamp
    tail = "加一个正文%s" %timestamp
    urlxx = saveBlog(s, title, tail)
    postid = getPostid(urlxx)
    deleteBlog(s, postid)









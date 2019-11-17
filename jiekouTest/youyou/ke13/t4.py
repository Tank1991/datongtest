# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re

def login(s, aaa, user, psw):
    '''fuction:
         登录拉勾网
    args：
        s：用来传s = requests.session()
        aaa: get_token()函数返回值：{"X_Anti_Forge_Token":"xx","X_Anti_Forge_Code":"xxx"}

    '''
    url2 = 'https://passport.lagou.com/login/login.json'
    h2 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
          "X-Requested-With": "XMLHttpRequest",
          "X-Anit-Forge-Token": aaa["X_Anti_Forge_Token"],
          "X-Anit-Forge-Code": aaa["X_Anti_Forge_Code"],
          "Referer": "https://passport.lagou.com/login/login.html"}

    body ={"isValidate": "true",
           "username": user,
           "password": psw,
           "request_form_verifyCode": "",
           "submit": ""}

    # s = requests.session()
    s.headers.update(h2)  # 更新s里面的头部
    r2 = s.post(url2, data=body)
    try:
        result = r2.json()
    except:
        result = r2.text
    return result

if __name__ == "__main__":
    from ke13.lgw import get_token
    s = requests.session()
    r = get_token(s)
    print(r)
    result = login(s, aaa=r, user="15221401012", psw="1111111")
    print("登录结果：%s"%result)

    submitToken = result['submitToken']
    print(submitToken)



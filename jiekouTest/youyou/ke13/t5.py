# coding:utf-8

import requests
from bs4 import BeautifulSoup
import re

# s = requests.session()

class LaGouWang():

    def __init__(self, s):
        self.s = s

    def get_token(self):
        '''fuction:
             获取拉勾网token和code两个参数
        args：
            s：用来传s = requests.session()
        return:
            {"X_Anti_Forge_Token":"xx","X_Anti_Forge_Code":"xxx"}
        '''
        url = "https://passport.lagou.com/login/login.html"
        h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
        }
        r1 = self.s.get(url, headers=h, verify=False) # headers=h, verify=False
        # print(r1.text)
        soup = BeautifulSoup(r1.content, "html.parser")
        all = soup.find_all("script")
        a = all[1].string
        # print(a)
        res = {}
        try:
            X_Anti_Forge_Token = re.findall("Token = \'(.+?)\'", a)
            # print(X_Anti_Forge_Token[0])
            res["X_Anti_Forge_Token"] = X_Anti_Forge_Token[0]
            X_Anti_Forge_Code = re.findall("Code = \'(.+?)\'", a)
            # print(X_Anti_Forge_Code[0])
            res["X_Anti_Forge_Code"] = X_Anti_Forge_Code[0]
        except:
            print("获取token和codes失败了，给个空字符串")
            res["X_Anti_Forge_Token"] = ""
            res["X_Anti_Forge_Code"] = ""
        return res

    def login(self, aaa, user, psw):
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
        self.s.headers.update(h2)  # 更新s里面的头部
        r2 = self.s.post(url2, data=body)
        try:
            result = r2.json()
        except:
            result = r2.text
        return result


if __name__ == "__main__":
    s = requests.session()
    t = LaGouWang(s)
    res = t.get_token()
    print(res)
    result = t.login(res, user="15221556302", psw="22222111")
    print(result)
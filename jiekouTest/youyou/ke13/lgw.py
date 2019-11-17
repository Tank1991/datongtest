# coding:utf-8

import requests
from bs4 import BeautifulSoup
import re

# s = requests.session()

def get_token(s):
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
    r1 = s.get(url, headers=h, verify=False) # headers=h, verify=False
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
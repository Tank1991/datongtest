# coding:utf-8
import requests
import re
# 禅道登录案例
# s = requests.session()

# host作为一个全局变量单独拿出来,以免测试服务器变更后，代码维护麻烦
host = "http://127.0.0.1"


def is_login_sucess(result):
    if "登录失败" in result:
        print("登录失败了！！！！")
        return False
    elif "parent.location" in result:
        print("登录成功了！！！！")
        return True
    else:
        print("其它情况，登录失败了！！")
        return False
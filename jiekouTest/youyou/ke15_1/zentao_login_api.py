# coding:utf-8
import requests
import re
# 禅道登录案例
# s = requests.session()

# host作为一个全局变量单独拿出来,以免测试服务器变更后，代码维护麻烦
host = "http://127.0.0.1"

def login(s, user, psw):
    url = host+"/zentao/user-login.html"

    h ={
        "Content-Type": "application/x-www-form-urlencoded"
       }
    body = {
        "account": user,
        "password": psw,
        "referer": "http://127.0.0.1/zentao/my/",
        "keepLogin[]": "on"
          }

    r = s.post(url, headers=h, data=body) # url, headers=h, data=body
    # print(r.status_code)
    # print(r.text)  # 如果.text出现乱码
    # print(r.content.decode("utf-8"))
    return r.content.decode("utf-8")

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

if __name__ == "__main__":
    s = requests.session()
    user = "admin1111"
    psw = "e10adc3949ba59abbe56e057f20f883e"
    result = login(s, user, psw)
    print(result)

    login_result = is_login_sucess(result)
    print("111111111111")
    print(login_result)


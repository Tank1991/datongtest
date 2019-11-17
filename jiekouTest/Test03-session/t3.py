#coding :utf-8

import requests
import urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup

#登录拉勾网

s = requests.session()

url = "https://passport.lagou.com/login/login.html"
h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"

}

r1 = s.get(url,headers=h,verify=False)
print(r1.content.decode("utf-8"))



body = {
    "isValidate": "true",
    "username": "13236271078",
    "password": "990eb670f81e82f546cfaaae1587279a",
    "request_form_verifyCode": "",
    "challenge": "73ff9b80741f76a86bef30e974b6e425"
    }
# r = s.post(url,data=body,verify=False)
# print(r.content.decode("utf-8"))






# </script>
#
#     <!-- 页面样式 -->    <!-- 动态token，防御伪造请求，重复提交 -->
#     <script>
#     window.X_Anti_Forge_Token = '66ebb402-8ef6-4ac1-9441-f87d41b791eb';
#     window.X_Anti_Forge_Code = '27362174';
# </script>



















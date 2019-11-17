# coding:utf-8

import requests

# 登录拉勾网案例

s = requests.session()
url = "https://passport.lagou.com/login/login.html"
# 伪造User-Agent
h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }

r1 = s.get(url, headers=h, verify=False)

print(r1.content.decode("utf-8"))



body = {
    "isValidate": "true",
    "username": "13249263211",
    "password": "c47eeb69fa4e64971fb29cb1e9163a19",
    "submit": "",
    "request_form_verifyCode": ""
   }

h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "X-Anit-Forge-Code":"111111111",
    "X-Anit-Forge-Token": "1164c7bf-24d0-485b-9de8-83f4a17a0d5f"
}

r = s.post(url, data=body, headers=h , verify=False)
print(r.status_code)
print(r.content.decode("utf-8"))


# X-Anit-Forge-Code: 69939467
# X-Anit-Forge-Token: 7364c7bf-24d0-485b-9de8-83f4a17a0d5f

'''
    <!-- 页面样式 -->    <!-- 动态token，防御伪造请求，重复提交 -->
    <script>
    window.X_Anti_Forge_Token = 'ef2d19b5-8b26-4eea-9ac0-31626ad31e97';
    window.X_Anti_Forge_Code = '47614215';

'''
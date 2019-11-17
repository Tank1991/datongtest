# coding:utf-8
import requests

s = requests.session()
print(s.cookies)
url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

# cook = {".CNBlogsCookie": "9A9A9767628321FDDD1521002C2E0A38D912B6DF436B1C43CAE99790D4ED4598E2198DD249BDE472F0D91B65DF954A8F205919F6E7609720A7DC3838C9419B37BB41305C2AFB7FFA3C77E879AC638BB4C42BD9B1",
#         ".Cnblogs.AspNetCore.Cookies": "CfDJ8FHXRRtkJWRFtU30nh_M9mD-9nTu9zUNwnJoeK1GjMRJXGOi_YGGwFBhFTYaHcYFHl8ZxDRSDzSWLVx98mfYxU1JvByntmvfhRKFq4ZdYHcC7QftD4SFxP60KfSTMyRk9ynpLRblOTItifIF_MdGLJzXGPNkzn8XN-11eFUFiCnb__99Lf3WYeuIPj_hqVJ_reviYZRSX2VtQNO78imwQ0nuS8v5P2avHkybBnE0Azp9YfLUf45dL9TAtxL2el7h71s5ZKfYBi0I86Qp3DjFDgO-dONs3htsVaSy7Twb1FNTvgbJKKHJRlkMBQQ49m8oVg"
#         }
# 往s里面更新cookies, 绕过验证码登录
c = requests.cookies.RequestsCookieJar()  # jar包
c.set(".CNBlogsCookie", "自己抓包" )
c.set(".Cnblogs.AspNetCore.Cookies", "自己抓包")
s.cookies.update(c)

# 看是不是更新过去了
print(s.cookies)

r1 = s.get(url, verify=False)
print(r1.text)

h = {
    "token": "xxxxxxxxxxxxx"
    }
token = "xxxxxxxx1111111"

url = "http://xxx.com/xx?token=xxxxxxxx1111111"

body = {
       "token": "xxxxxxxxxxx",
        "a": "xxx",
        "b": "xxx"
       }

import requests

s = requests.session()

# 全局设置verify = False
s.verify = False

print(s.cookies)


url = "https://eledata.superboss.cc/jump.jsp"
r1 = s.get(url)
print(s.cookies)

r2 = s.get(url)

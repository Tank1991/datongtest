#coding:utf-8

import  requests
import  urllib3

urllib3.disable_warnings()
url = "https://www.baidu.com/"


r = requests.get(url,verify = False) # verify = False


print(r.status_code)



















































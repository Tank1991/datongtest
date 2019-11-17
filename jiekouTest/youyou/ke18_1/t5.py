import requests
import json

s = requests.session()

url = "http://httpbin.org/post"

j = {"a": 111, "b": 222 , "c": True, "d": None}


body = {
    "params": json.dumps(j)
}
print(body)

r1 = s.post(url, data=body)
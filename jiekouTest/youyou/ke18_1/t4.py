import requests
s = requests.session()

url = "http://httpbin.org/post"

# 字典key是唯一的
body = [
        ("a", "111"),
        ("b", "222"),
        ("c", "ccc"),
        ("a","22222")
        ]

r = s.post(url, params=body)
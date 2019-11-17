# coding:utf-8
import requests

s = requests.session()

h = s.headers
print(h)

h1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
s.headers.update(h1)

h2 = s.headers
print(h2)

r1 = s.get("http://127.0.0.1/zentao/bug-browse-1.html")

r2 = s.get("http://127.0.0.1")

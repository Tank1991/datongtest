# coding:utf-8
import json

# print(help(json))
a = None
print(type(a))

aa = json.dumps(a)
print(type(aa))
print(aa)   # null

b = False
print(type(b))
bb = json.dumps(b)
print(type(bb))
print(bb)

# 所有的json格式都是字符串
c = "hello world"
print(json.dumps(c))

d = [None, 112, "hello", True]
e = (None, 112, "hello", True)
print(json.dumps(d))

f = {
    "a": None,
    "b": True,
    "c": 12,
    "d": "hello",
    "e": [1, 2, 3],
    "f": (None, True, "11"),
    "g": {
        "a": 111,
        "b": True
        }
    }
# f是dict, h是str
h = json.dumps(f)
print(h)
# 接口文档里面 post
# body 传json格式  {  }  95%以上
# 如： [{"a": true, "b": null}]  # json格式

qq = [{"a": True, "b": None}]
print(json.dumps(qq))  # [{"a": true, "b": null}]





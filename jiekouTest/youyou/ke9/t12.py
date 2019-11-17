# coding:utf-8
import json

# json格式的字符串，类似于python里面的list
a = '[{"a": true, "b": null}]'  # json格式的字符串
# 转list
print(json.loads(a))  # list

# b是一个类似于dict类型的json数据，本质上是str
b = '{"e": [1, 2, 3], "g": {"a": 111, "b": true}, "a": null, "b": true, "f": [null, true, "11"], "d": "hello", "c": 12}'
print(json.loads(b))




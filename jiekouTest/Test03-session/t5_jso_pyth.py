# coding:utf-8
import json

#json 格式的字符串
a = '[{"a" : true, "b" : null }]'
#转成list
print(json.loads(a))

# b是一个类似于dict类型的json数据，本质是str
b = '{"e": [1, 2, 3], "g": {"a": 111, "b": true}, "a": null, "b": true, "f": [null, true, "11"], "d": "hello", "c": 12}'
print(json.loads(b))

c = {"a":True ,"b":None}
print(str(c))
print(json.dumps(c))

# python 标准dict格式字符串
d = '{"a":True ,"b":None}'
print(eval(d))

# json 格式的dict 字符串
e = '{"a": true, "b": null}'
print(json.loads(e))








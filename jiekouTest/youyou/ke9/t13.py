import json
a = {"a": True, "b": None}
print(str(a))
# json格式的字符串
print(json.dumps(a))

b = '{"a": True, "b": None}'  # python标准dict格式字符串
# 转字典？
print(eval(b))


c = '{"b": null, "a": true}'  # json格式的dict字符串
# 转字典
print(json.loads(c))

d = '{"hello": "wolrd!"}'
print(eval(d))
print(json.loads(d))
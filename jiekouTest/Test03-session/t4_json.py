#coding:utf-8
import json

a = None

aa = json.dumps(a)
print(type(aa))
print(aa)

b = False
print(type(b))
bb = json.dumps(b)
print(type(bb))
print(bb)

#所有的json都是字符串

c = [None ,1,2,3,"a",True]
print(json.dumps(c))

d = {
    "a ":None,
    "b":True,
    "c":12,
    "d":"hello",
    "e":[1 ,2 ,3],
    "f":(None , True ,"11"),
    "g":{
        "a ":111,
        "b":True
         }
    }
print(json.dumps(d))











































































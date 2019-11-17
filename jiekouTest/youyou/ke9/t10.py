# coding:utf-8

a = None   # SQL null
print(a)

b = 12
c = 12.01
print(b)
print(type(b))
d = "12"
print(d)
print(type(d))

e = True
f = False

g = []  # list  可变的对象
print(type(g))
print(g)
g.append(a)
g.append(b)
g.append([1, 23, 4])
print(g)
print(g[1])

h = (1, 3)  # tuple 不可变的对象
print(type(h))
q = h[-1]

w = {
    "a": "",
    "b": 11,
    'c': 11,
    1: "11111111",
    "aa": {
              "a": "11111111"
            }
    }
# 1.字典key是唯一的，2.字典是无序的,3.单引号和双引号不分
print(w)
print(w["c"])


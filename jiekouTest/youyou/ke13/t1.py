# coding:utf-8
from bs4 import BeautifulSoup
yo = open("yoyo.html", "r")
# print(yo.read())

soup = BeautifulSoup(yo, "html.parser")

# 有多个标签时候
all = soup.find_all("a")  # 符合所有查找条件的
print(all)
print(all[1])
for i in all:
    print(i)

# a = soup.a
# print(a)
# att = a.attrs  # 属性转字典
# print(att)
#
# print(att['href'])
# # class属性可以有多个
# print(att['class'])  # list
# print(att['id'])








# print(type(soup))

# # print(soup.prettify())
# # 获取完整的标签
# tag1 = soup.title # tag对象
# print(tag1)
# # 标签里面的string
# # print(tag1.string)
#
# tag2 = soup.p  # 有多个标签一样，获取的是第一个
# print(tag2)
#
# print(tag2.b.string)



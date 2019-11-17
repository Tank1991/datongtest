#coding:utf-8
from bs4 import BeautifulSoup

yo = open("yoyo.html", "r")
# print(yo.read())

soup = BeautifulSoup(yo, "html.parser")
# print(soup.prettify())

tag1 = soup.title
# print(tag1)
# print(tag1.string)


tag2 = soup.p      #有多个对象的时候，只会显示第一个
# print(tag2)
# print("tag2的精准定位-- "+tag2.b.string)

a = soup.a
print(a)
att = a.attrs    #属性转化为字典
print(att)
print(att["href"])
print(att["class"])     #可能有多个class


#有多个标签的情况
a_all =soup.find_all("a")
print(a_all)
for i in a_all:
    print(i)

























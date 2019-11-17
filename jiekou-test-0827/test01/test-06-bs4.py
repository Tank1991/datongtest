# coding:utf-8
import requests
from  bs4 import BeautifulSoup

file01 = open("xxx.html" , "r")     #读取html文件

soup = BeautifulSoup(file01 , "html.parser")

print(soup.prettify())     #将html展示出层级关系

#获取标签  tag   <a  href = "">新闻<b>我的文字</></a>
soup.a      #标签对象    如果有多个一样的名称，只可以获取到第一个
soup.a.b      #获取一个标签里面的子标签

#获取标签里面的文字string   新闻
soup.a.string

#获取标签的属性    href = ""
soup.a.attrs

#获取所有的同样的标签    获取所有的a标签   list对象
aa = soup.find_all(class_ = "content")     #有冲突class

# 获取tag标签下的所有的文本
bb = aa.get_text()

#    replace替换字符串里面的特殊的字符串
aa.get_text().replace("\n" , "")







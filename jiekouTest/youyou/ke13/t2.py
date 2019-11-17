from bs4 import BeautifulSoup
import requests


r1 = requests.get("https://www.qiushibaike.com/", verify=False)

soup = BeautifulSoup(r1.content, "html.parser")
# class跟python系统关键字冲突
all = soup.find_all(class_="content")  # class_="content"
for i in all:
    print(i.span.get_text().replace("\n", ""))  # 获取当前节点下，子孙节点字符串
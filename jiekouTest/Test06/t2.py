#coding:utf-8
from bs4 import BeautifulSoup
import  requests
import urllib3
urllib3.disable_warnings()

r = requests.get("https://www.qiushibaike.com/", verify=False)

soup = BeautifulSoup(r.content, "html.parser")

all_class = soup.find_all(class_="content") #class_="content"   class的下划线跟关键字class重复

for i in all_class:
    print(i.span.get_text().replace("\n", ""))       # 获取当前节点下，子孙节点字符串























































































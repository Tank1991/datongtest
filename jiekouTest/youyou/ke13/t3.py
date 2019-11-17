from bs4 import BeautifulSoup
import requests


r1 = requests.get("http://699pic.com/sousuo-218808-13-1.html", verify=False)

soup = BeautifulSoup(r1.content, "html.parser")
all = soup.find_all(class_="lazy")
for i in all:
    # 异常情况处理
    try:
        jpg_url = i["data-original"]  # tag对象取属性
        print(jpg_url)
        jpg_title = i["title"]
        print(jpg_title)

        r2 = requests.get(jpg_url)
        with open(jpg_title+".jpg", "wb") as fp:
            fp.write(r2.content)
    except:
        pass





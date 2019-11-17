# coding:utf-8
import requests
from ke15_1.zentao_login_api import login
import time
host = "http://127.0.0.1"

def send_img(s, filename="yoyo11.jpg"):
    url_sendimg = host+"/zentao/file-ajaxUpload-5b66e82c42a91.html?dir=image"

    f = {"loclUrl": (None, filename),
         "imgFile": (filename, open(filename, "rb"), "image/jpeg")
        }

    # 文件上传，files = body

    r2 = s.post(url_sendimg, files=f)
    try:
        print(r2.json())
        return r2.json()
    except:
        print("图片上传失败：%s"%r2.text)
        return r2.text

def add_bug(s, jpg_url):
    '''提交bug'''
    timestemp = str(time.time())
    url_add_bug = host+"/zentao/bug-create-1-0-moduleID=0.html"
    body = {
            "product": "1",
            "module": "0",
            "project": "",
            "openedBuild[]": "trunk",
            "assignedTo": "admin",
            "type": "codeerror",
            "os": "all",
            "browser": "all",
            "color": "",
            "title": "yoyoketang-%s"%timestemp,
            "severity": "3",
            "pri": "0",
            "steps": '<img src="%s" alt="" /><p>[步骤]</p>\
                    <p>[结果]</p>\
                    <p>[期望]</p>' % jpg_url,
            "story": "0",
            "task": "0",
            "mailto[]": "",
            "keywords": "",
            "uid": "5a2955c884f98",
            "case": "0",
            "caseVersion": "0",
            "result": "0",
            "testtask": "0"
            }
    r = s.post(url_add_bug, data=body)
    print(r.content.decode("utf-8"))


def send_file_and_add_bug(s, jpg_url, filename1,filename2):
    send_file_url = host+"/zentao/bug-create-1-0-moduleID=0.html"
    timestemp = str(time.time())

    title = "yoyoketang-%s"%timestemp
    body = {
            "product": "1",
            "module": "0",
            "project": "",
            "openedBuild[]": "trunk",
            "assignedTo": "admin",
            "type": "codeerror",
            "os": "all",
            "browser": "all",
            "color": "",
            "title": title,
            "severity": "3",
            "pri": "0",
            "steps": '<img src="%s" alt="" /><p>[步骤]</p>\
                    <p>[结果]</p>\
                    <p>[期望]</p>' % jpg_url,
            "story": "0",
            "task": "0",
            "mailto[]": "",
            "keywords": "",
            "uid": "5a2955c884f98",
            "case": "0",
            "caseVersion": "0",
            "result": "0",
            "testtask": "0"
            }

    # 单个附件
    # f = {"labels[]": (None, name),
    #      "files[]": (filename, open(filename, "rb"), "image/jpeg")
    #     }
    #
    fs = [("labels[]", (None, "yoyo")),
          ("files[]", (filename1, open(filename1, "rb"), "image/jpeg")),

          ("labels[]", (None, "yoyo11")),
          ("files[]", (filename2, open(filename2, "rb"), "image/jpeg")),
        ]



    r3 = s.post(send_file_url, data=body, files=fs)
    print(r3.content.decode("utf-8"))

    print("添加Bug的tile：%s" % title)
    return title

def is_add_bug_sucess(s, title):
    '''判断bug是否提交成功'''
    url11 = host+"/zentao/bug-browse-1.html"
    r111 = s.get(url11)
    buglist = r111.content.decode("utf-8")
    if title in buglist:
        print("提交成功了")
        return True
    else:
        print("提交失败了")
        return False

if __name__ == "__main__":
    s = requests.session()
    result = login(s, "admin", "e10adc3949ba59abbe56e057f20f883e")
    print(result)
    jpg_url = send_img(s, "yoyo.jpg")['url']

    print(jpg_url)
    # add_bug(s, jpg_url)
    title = send_file_and_add_bug(s, jpg_url, "yoyo.jpg", "yy.jpg")
    url11 = "http://127.0.0.1/zentao/bug-browse-1.html"
    r111 = s.get(url11)
    buglist = r111.content.decode("utf-8")
    # print(r111.content.decode("utf-8"))
    result = is_add_bug_sucess(s, title)
    print(result)







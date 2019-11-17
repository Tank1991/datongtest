# coding:utf-8
import requests
import time
host = "http://127.0.0.1"

class SendFile():
    def __init__(self, s):
        self.s = s

    def sendImg(self, jpgpath, jpgname="1.jpg", jpgtype='image/jpeg'):
        url2 = host+'/zentao/file-ajaxUpload-5b0a9f621253b.html?dir=image '
        body = {
            "localUrl": (None, jpgname),
            "imgFile": (jpgname, open(jpgpath, "rb"), jpgtype)
            }

        # 上传图片的时候，不要用data和json
        r2 = self.s.post(url2, files=body)  # files
        print(r2.text)
        try:
            jpg_url = r2.json()["url"]
            print(jpg_url)
            return jpg_url
        except Exception as msg:
            print("图片上传失败,原因：%s" %msg)
            return ''

    def addBug(self, jpgpath=None):
        timestemp = str(time.time())
        # jpgpath = "data/upload/1/201805/2721190806893t32.jpg"
        # 提交bug, 带上附件
        url1 = host+"/zentao/bug-create-1-0-moduleID=0.html"
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
            "title": "yoyoketang-%s" % timestemp,
            "severity": "3",
            "pri": "0",
            "steps": '<p>[步骤]</p>\
                    <p>1、第一步点</p>\
                    <p>2、第二步点</p>\
                    <p>3、点三步点</p>\
                    <p>[期望]222<img src="%s" alt="" /></p>\
                    <p>[结果]</p>\
                    <p>[期望]</p>' % jpgpath,
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
        r = s.post(url1, data=body)

        print(r.content)


if __name__ == "__main__":
    s = requests.session()
    from apipage.login_zentao import LoginZentao
    # 先调用登录方法
    login = LoginZentao(s)
    login.login()

    # 上传文件
    send = SendFile(s)
    jpgurl = send.sendImg("46.png", jpgname="46.png")

    # 提交bug
    send.addBug(jpgurl)





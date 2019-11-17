#coding;utf-8
import unittest
import requests

class TeatQQ(unittest.TestCase):

    def test_qq_01(self):
        url = "http://japi.juhe.cn/qqevaluate/qq"

        par = {
            "key":"8dbee1fcd8627fb6699bce7b986adc45",
            "qq":"1173540745"
        }

        # r = requests.get(url,params=par)
        r = requests.post(url,params=par)

        #实际结果  代码运行后的结果
        code_shiji = r.status_code
        print(code_shiji)
        print("Set-Cookie :"+ r.headers["Set-Cookie"])
        res = r.json()
        print(res)

        #所有的测试结果判断都可以用法True 和False来判定
        #期望结果   没有运行结果时候就有的期望值
        qiwang = 200

        #断言就是 实际结果和期望结果的比较
        self.assertTrue(res['reason'] == "success")
        self.assertTrue(code_shiji == qiwang)


        # if code == 200 :
        #     print("测试通过！")
        # else :
        #     print("测试失败！")

if __name__ == '__main__':
    unittest.main()










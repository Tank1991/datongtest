# coding:utf-8
import requests
import unittest
import ddt
from ke15_1.zentao_login_api import *
from ke16.readexcel import ExcelUtil
# data1 = [{"user": "admin", "psw": "e10adc3949ba59abbe56e057f20f883e", "expect": True},
#          {"user": "admin2", "psw": "222222", "expect": False},
#          {"user": "admin111", "psw": "e10adc3949ba59abbe56e057f20f883e", "expect": True},
#          {"user": "admin4", "psw": "33333", "expect": False},
#          ]


d = ExcelUtil("data.xlsx", sheetName="Sheet1")
data1 = d.dict_data()
print(data1)

@ddt.ddt
class Test(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    @ddt.data(*data1)
    def test_(self, aaaa):
        print("测试用例数据：%s"%aaaa)
        user = aaaa['user']
        psw = aaaa['psw']
        result = login(self.s, user, psw)
        print(result)
        login_result = is_login_sucess(result)
        print("实际结果：%s" % login_result)  # 实际结果 bool
        expect = aaaa['expect']   # str

        self.assertTrue(str(login_result) == expect)

if __name__ == "__main__":
    unittest.main()





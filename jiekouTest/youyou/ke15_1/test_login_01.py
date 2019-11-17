# coding:utf-8
import unittest
from ke15_1.zentao_login_api import *

class TestLogin(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.s = requests.session()
    #

    def setUp(self):
        self.s = requests.session()

    def test_01(self):
        '''登录成功测试:正确账号，正确密码'''
        user = "admin"
        psw = "e10adc3949ba59abbe56e057f20f883e"
        result = login(self.s, user, psw)
        print(result)
        login_result = is_login_sucess(result)
        print("111111111111")
        print(login_result)
        self.assertTrue(login_result)

    def test_02(self):
        '''登录失败测试:错误账号，错误密码'''
        user = "admin111"
        psw = "1e10adc3949ba59abbe56e057f20f883e"
        result = login(self.s, user, psw)
        print(result)
        login_result = is_login_sucess(result)
        print("111111111111")
        print(login_result)
        self.assertFalse(login_result)

    def tearDown(self):
        self.s.cookies.clear()

if __name__ == "__main__":
    unittest.main()




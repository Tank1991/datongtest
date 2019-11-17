# coding:utf-8
import unittest
from ke15_1.zentao_login_api import *
from ke15_1.reslut import  *
class TesttiBug(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def test_01(self):
        '''登录成功测试:正确账号，正确密码'''
        user = "admin"
        psw = "e10adc3949ba59abbe56e057f20f883e"
        result = login(self.s, user, psw)
        login_reslut = is_login_sucess(result)
        print("登录的结果判断：%s" % login_reslut)










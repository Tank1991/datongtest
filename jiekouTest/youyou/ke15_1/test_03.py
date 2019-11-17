# coding:utf-8
import unittest
from ke15_1.lgw_login_api import LoginLgw
import requests
class TesttiBug(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.lgw = LoginLgw(self.s)

    def test_01(self):
        '''登录成功测试:正确账号，正确密码'''
        user = "1522142101"
        psw = "111111111"
        self.lgw.login(user, psw)


import unittest
from  appium import webdriver
import time
from common.baseapp import Base
desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "appPackage": "com.yipiao",
                "noReset": True,
                "appActivity": "com.yipiao.activity.LaunchActivity"
                }


class TestYaoQing(unittest.TestCase):
    loc1 = {"name": "我的", "by": "text", "value": "我的"}
    loc2 = {"name": "邀请好友", "by": "text", "value": "邀请好友"}
    loc3 = {"name": "邀请好友-弹出文本", "by": "id", "value": "com.yipiao:id/socialize_text_view"}
    loc4 = {"name": "取消分享", "by": "text", "value": "取消分享"}

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.driver.wait_activity("com.yipiao/com.zt.train.activity.MainActivity", 15)
        cls.app = Base(cls.driver)
        # 先判断“下次再说”是否存在
        tan_loc = {"name": "下次再说", "by": "text", "value": "下次再说", "timeout": "5"}
        if cls.app.is_element_exist(tan_loc):
            cls.app.click(tan_loc)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def get_result(self):
        # 获取结果
        result = []
        els = self.app.finds(self.loc3)
        for i in els:
            t = i.text
            result.append(t)
        print(result)
        return result

    def test_01(self):
        '''我的-邀请好友'''
        self.app.click(self.loc1)
        self.app.click(self.loc2)
        # 获取结果
        result = self.get_result()
        self.app.click(self.loc4)  # 点取消分享
        expresult = ["微信", "朋友圈", "QQ", "QQ空间", "短信"]
        self.assertTrue(result == expresult)

if __name__ == "__main__":
    unittest.main()
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def is_toast_exist(driver, _text):
    # loc = ("xpath", '//*[@text="%s"]'%_text)
    loc = ("xpath", './/*[contains(@text, "%s")]'%_text)
    try:
        ele = WebDriverWait(driver, 10, 0.3).until(EC.presence_of_element_located(loc))
        t = ele.text
        print(t)
        if _text in t:
            return True
        else:
            return False
    except:
        return False

des = {
        'platformName': 'Android',   # 手机是Android还是ios
        'deviceName': 'emulator-5554',
        'platformVersion': '5.1.1',  # android版本号
        # apk包名  # aapt工具查看
        'appPackage': 'com.taobao.taobao',
        'noReset': True,
        # apk的launcherActivity
        'appActivity': 'com.taobao.tao.welcome.Welcome',
        "automationName": "Uiautomator2"
        }

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des)
time.sleep(15)

driver.back()  # 返回键
result = is_toast_exist(driver, "再按一次返回键退出手机淘宝")

assert result==True  # python自带的断言

# unittest里面断言 self.assertTrue(result==True)

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from common.baseapp import Base
des = {
        'platformName': 'Android',   # 手机是Android还是ios
        'deviceName': 'emulator-5554',
        'platformVersion': '5.1.1',  # android版本号
        # apk包名  # aapt工具查看
        'appPackage': 'com.taobao.taobao',
        'noReset': True,
        # apk的launcherActivity
        'appActivity': 'com.taobao.tao.welcome.Welcome'
        }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des)
time.sleep(20)
driver.wait_activity("com.taobao.tao.homepage.MainActivity3", 20)


from common.appkey import key
# Android only
driver.keyevent(key.KEYCODE_HOME)  # 返回键
time.sleep(10)



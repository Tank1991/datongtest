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

# 获取当前页面activity
act = driver.current_activity
print(act)  # com.taobao.tao.homepage.MainActivity3

loc_text = {"by": "text", "value": '注册/登录'}
app = Base(driver)
app.find(loc_text).click()

act1 = driver.current_activity
print(act1)


time.sleep(3)
loc_2 = {"by": "desc", "value": "帮助"}
app.find(loc_2).click()

act2 = driver.current_activity
print(act2)

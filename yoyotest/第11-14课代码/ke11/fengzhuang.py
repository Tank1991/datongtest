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

# loc_login = 'text("注册/登录")'
# driver.find_element_by_android_uiautomator(loc_login).click()


# loc_1 = {"by": "android", "value": 'text("注册/登录")'}

loc_text = {"by": "text", "value": '注册/登录'}
app = Base(driver)
app.find(loc_text).click()
time.sleep(3)
loc_2 = {"by": "desc", "value": "帮助"}
app.find(loc_2).click()

#
# loc_3 = {"by": "text", "value": "帮助"}
# loc_4 = {"by": "id", "value": "xxxx"}
# loc_5 = {"by": "class name", "value": "xxxx"}


# loc_help = 'description("帮助")'
# driver.find_element_by_android_uiautomator(loc_help).click()
# time.sleep(5)

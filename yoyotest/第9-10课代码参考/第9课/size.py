from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
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
time.sleep(25)

loc_login = 'text("注册/登录")'
el = driver.find_element_by_android_uiautomator(loc_login)

# 手机当前的分辨率
a = driver.get_window_size()
print(a)  # {'height': 1280, 'width': 720}

# loction
loct = el.location
print(loct)  # {'x': 520, 'y': 1108}

size = el.size
print(size)   # {'height': 56, 'width': 176}

# 600, 1130

# 跟据手机分辨率自动算出手机的相对位置

# 如果click失效的时候，可以用tap(针对于native_app)
action = TouchAction(driver)
action.tap(el).perform()






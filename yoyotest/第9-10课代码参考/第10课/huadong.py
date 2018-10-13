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
time.sleep(20)

def swipeUp(driver, duration=500):
    # 手机当前的分辨率
    a = driver.get_window_size()
    print(a)  # {'height': 1280, 'width': 720}
    start_x = a['width']/2
    start_y = a['height']/5*4

    end_x = a['width']/2
    end_y = a['height']/5*1

    # 往上滑动
    driver.swipe(start_x, start_y, end_x, end_y, duration)

def swipeDown(driver, duration=500):
    a = driver.get_window_size()
    print(a)  # {'height': 1280, 'width': 720}
    start_x = a['width']/2
    start_y = a['height']/5*1
    end_x = a['width']/2
    end_y = a['height']/5*4
    # 往下滑动
    driver.swipe(start_x, start_y, end_x, end_y, duration)


swipeUp(driver)
time.sleep(3)
swipeDown(driver)


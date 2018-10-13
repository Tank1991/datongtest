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
# time.sleep(20)
driver.wait_activity("com.taobao.tao.homepage.MainActivity3", 20)


loc_text = {"by": "text", "value": '注册/登录'}
app = Base(driver)
app.find(loc_text).click()

time.sleep(10)

# setup里面，让用例从起点开始
driver.start_activity("com.taobao.taobao", "com.taobao.tao.homepage.MainActivity3")

# # 切换到某个activity
# driver.start_activity("com.taobao.taobao", "com.ali.user.mobile.login.ui.UserLoginActivity")

time.sleep(10)
driver.quit()

# loc_text = {"by": "text", "value": '注册/登录'}
# app = Base(driver)
# app.find(loc_text).click()

'''
com.taobao.tao.homepage.MainActivity3
com.ali.user.mobile.login.ui.UserLoginActivity
com.ali.user.mobile.webview.WebViewActivity
'''
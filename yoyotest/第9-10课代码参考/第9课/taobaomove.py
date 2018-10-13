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

loc_login = 'text("注册/登录")'
driver.find_element_by_android_uiautomator(loc_login).click()
time.sleep(3)
loc_help = 'description("帮助")'
driver.find_element_by_android_uiautomator(loc_help).click()
time.sleep(5)

# webview不需要切换
xpath_loc = '//android.webkit.WebView[@content-desc="安全验证"]/android.view.View[4]'
start = driver.find_element_by_xpath(xpath_loc)

action = TouchAction(driver)
action.press(start).wait(500).move_to(x=620, y=0).wait(1000).release().perform()




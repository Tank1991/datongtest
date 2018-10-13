# coding=utf-8
from appium import webdriver
import time
desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "appPackage": "com.taobao.taobao",
                "appActivity": "com.taobao.tao.welcome.Welcome",
                "noReset": True
                }

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(10)

# # text文本定位
# loc_login = 'text("注册/登录")'
# driver.find_element_by_android_uiautomator(loc_login).click()
# time.sleep(2)

# className

loc_login = 'className("android.widget.Button")'
driver.find_element_by_android_uiautomator(loc_login).click()


# resourceId
loc_input_user = 'resourceId("com.taobao.taobao:id/aliuser_login_mobile_et")'
driver.find_element_by_android_uiautomator(loc_input_user).send_keys("12345678")

# description
loc_help = 'description("帮助")'
driver.find_element_by_android_uiautomator(loc_help).click()


time.sleep(10)
driver.quit()






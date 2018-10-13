# coding=utf-8
from appium import webdriver
import time
desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "appPackage": "com.taobao.taobao",
                "appActivity": "com.taobao.tao.welcome.Welcome",
                "noReset": True,
                "automationName": "UiAutomator2"
                }

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(10)

# class_text

class_text = 'className("android.widget.Button").text("注册/登录")'
driver.find_element_by_android_uiautomator(class_text).click()

# 父子查找

# f_sun = 'resourceId("com.taobao.taobao:id/ll_search_bar_content").childSelector(text("扫一扫"))'
# driver.find_element_by_android_uiautomator(f_sun).click()

# 兄弟定位
time.sleep(3)
brother = 'text("请输入手机号码").fromParent(className("android.widget.TextView"))'
driver.find_element_by_android_uiautomator(brother).click()

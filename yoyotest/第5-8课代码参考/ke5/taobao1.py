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

# id定位
# driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
# time.sleep(3)
# driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
# driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys("yoyo")

# 通过文本text selenium->//*[text()="扫一扫"]
# driver.find_element_by_xpath('//*[@text="扫一扫"]').click()

# driver.find_element_by_xpath('//*[contains(@text, "扫一扫")]')
# driver.find_element_by_accessibility_id()
# driver.find_element_by_xpath('//*[@text="注册/登录"]').click()
# time.sleep(3)
# driver.find_element_by_accessibility_id("帮助").click()

# class定位
driver.find_element_by_class_name("android.widget.Button").click()

# list定位
driver.find_elements_by_class_name("android.widget.Button")[0].click()

driver.find_element_by_android_uiautomator()

time.sleep(20)
driver.quit()







# coding=utf-8
from appium import webdriver
import time
desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "appPackage": "com.taobao.taobao",
                "appActivity": "com.taobao.tao.welcome.Welcome",
                # "noReset": True
                }

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(10)
driver.find_element_by_id("com.taobao.taobao:id/uik_mdButtonDefaultPositive").click()


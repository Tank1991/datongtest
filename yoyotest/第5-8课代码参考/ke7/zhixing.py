# coding=utf-8
from appium import webdriver
import time
desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "appPackage": "com.yipiao",
                "noReset": True,
                "appActivity": "com.yipiao.activity.LaunchActivity"
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(10)
driver.find_element_by_android_uiautomator('text("我的")').click()
time.sleep(3)
driver.find_element_by_android_uiautomator('text("产品意见")').click()
time.sleep(3)

# 获取当前 上下文context
cur = driver.current_context
print(cur)
# 获取所有 上下文contexts
all = driver.contexts
print(all)

# 切换过去"WEBVIEW_com.yipiao"
driver.switch_to.context("WEBVIEW_com.yipiao")

# No Chromedriver found that can automate Chrome '39.0.0'

time.sleep(2)
# 确认是否切换获取了
cur2 = driver.current_context
print(cur2)

# 定位webview上的元素

# 保存页面信息到本地
h = driver.page_source
#
# with open("fankui.html", "wb") as f:
#     f.write(h.encode('utf-8'))


# 点webview上元素
driver.find_element_by_xpath('//*[contains(text(), "我能抢到票吗")]').click()


# # 切回到native_app
# driver.switch_to.context("NATIVE_APP")
# print(driver.current_context)

time.sleep(5)
driver.quit()






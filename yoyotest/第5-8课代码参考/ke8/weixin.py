from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '8.0.0',
    'deviceName': 'A5RNW18316011440',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    "automationName": "UiAutomator2",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "chromeOptions": {"androidProcess": "com.tencent.mm:tools"}
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)
# 点微信首页搜索按钮
driver.find_element_by_accessibility_id("搜索").click()
# 输入内容搜索
time.sleep(3)
driver.find_element_by_id("com.tencent.mm:id/jd").send_keys("yoyoketang")
# 点开公众号
print(driver.contexts)
time.sleep(3)
driver.find_element_by_id("com.tencent.mm:id/nr").click()
# 点公众号菜单-精品分类
print(driver.contexts)
time.sleep(3)
driver.find_elements_by_id("com.tencent.mm:id/af5")[0].click()
# 切换到webview
time.sleep(2)
print(driver.contexts)

driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")


# handles = driver.window_handles
# print(handles)
#
# driver.switch_to.window(handles[-1])
#
# # 保存源码到本地
# h = driver.page_source
# #
# with open("weixin.html", "wb") as f:
#     f.write(h.encode('utf-8'))
#
# # 点h5页面元素
# driver.find_element_by_xpath(".//*[@id='namespace_1']/div[1]/div/div[2]").click()




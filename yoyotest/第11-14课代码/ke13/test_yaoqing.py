import unittest
from  appium import webdriver
import time
from common.baseapp import Base
desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "appPackage": "com.yipiao",
                "noReset": True,
                "appActivity": "com.yipiao.activity.LaunchActivity"
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# adb shell dumpsys activity top | findstr ACTIVITY
driver.wait_activity("com.yipiao/com.zt.train.activity.MainActivity", 15)

app = Base(driver)

# 先判断“下次再说”是否存在
tan_loc = {"name": "下次再说", "by": "text", "value": "下次再说", "timeout": "5"}
if app.is_element_exist(tan_loc):
    app.click(tan_loc)

app.click({"name": "我的", "by": "text", "value": "我的"})

app.click({"name": "邀请好友", "by": "text", "value": "邀请好友"})
# 获取结果
result = []
els = app.finds({"name": "邀请好友-弹出文本", "by":"id", "value":"com.yipiao:id/socialize_text_view"})
for i in els:
    t = i.text
    result.append(t)
print(result)

app.click({"name": "取消分享", "by": "text", "value": "取消分享"})

expresult = ["微信", "朋友圈", "QQ", "QQ空间", "短信"]
assert result==expresult

driver.quit()
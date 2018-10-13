from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '8.0.0',
    'deviceName': 'A5RNW18316011440',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'automationName': 'Uiautomator2',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.a = self.driver.get_window_size()

    def swipeUp(self, duration=500, t=1):
        # 手机当前的分辨率
        print(self.a)  # {'height': 1280, 'width': 720}
        start_x = self.a['width']/2
        start_y = self.a['height']/5*4

        end_x = self.a['width']/2
        end_y = self.a['height']/5*1
        for i in range(t):
            # 往上滑动
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipeDown(self, duration=500, t=1):
        a = self.driver.get_window_size()
        print(a)  # {'height': 1280, 'width': 720}
        start_x = self.a['width']/2
        start_y = self.a['height']/5*1
        end_x = self.a['width']/2
        end_y = self.a['height']/5*4
        # 往下滑动
        for i in range(t):
             self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def tap_new(self, el=None, x=None, y=None, count=1):
        action = TouchAction(self.driver)
        if el is not None:
            action.tap(element=el, count=count).perform()  # 方法一 传元素对象
        else:
            action.tap(x=x, y=y, count=count).perform()

    def is_toast_exist(driver, _text):
        # loc = ("xpath", '//*[@text="%s"]'%_text)
        loc = ("xpath", './/*[contains(@text, "%s")]'%_text)
        try:
            ele = WebDriverWait(driver, 10, 0.3).until(EC.presence_of_element_located(loc))
            t = ele.text
            print(t)
            if _text in t:
                return True
            else:
                return False
        except:
            print("toast没找到！！！")
            return False



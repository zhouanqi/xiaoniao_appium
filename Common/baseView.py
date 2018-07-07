# -*- coding: utf-8 -*-
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction


class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,loc):
        return self.driver.find_element_by_android_uiautomator(loc)

    def find_element_xpath(self,loc):
        return self.driver.find_element_by_xpath(loc)

    def save_screenshotimg(self,imgname):
    	self.driver.get_screenshot_as_file('./imgname/'+imgname)

    def mobile_size(self):
        mobile_x = self.driver.get_window_size()['width']
        mobile_y = self.driver.get_window_size()['height']
        return mobile_x,mobile_y

    def swipe_screenxy(self,start_x,start_y,end_x,end_y):
        mobile_x, mobile_y=self.mobile_size()
        self.driver.swipe(mobile_x *start_x, mobile_y * start_y, mobile_x * end_x,mobile_y * end_y,
                     duration=2000)


#
# -*- coding: utf-8 -*-
from appium.webdriver.webdriver import WebDriver
class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,loc):
        return self.driver.find_element_by_android_uiautomator(loc)

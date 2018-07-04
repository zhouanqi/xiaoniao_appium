# -*- coding: utf-8 -*-
import logging
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver
from common.baseView import BaseView

class Login_func(BaseView):

    element=''

    def check_element(self,element):

        try:
            element_s=self.find_element(element)
        except NoSuchElementException:
            logging.info('no element:loginname,password,loginin')
        else:
            return element_s



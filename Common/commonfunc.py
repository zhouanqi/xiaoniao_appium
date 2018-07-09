# -*- coding: utf-8 -*-
import logging
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver
from common.baseView import BaseView

# BaseView.save_screenshotimg()
class Check_func(BaseView):

    def check_element(self,element,name):

        try:
            element_s=self.find_element(element)
        except NoSuchElementException as e:
            time.sleep(2)
            logging.warning('no element:%s'%name)
            return False
        else:
            time.sleep(0.5)
            return element_s

    def check_element_xpath(self, element ,name):

        try:
            element_s = self.find_element_xpath(element)
        except NoSuchElementException as e:
            time.sleep(2)
            logging.warning('no element:%s' % name)
            return False
        else:
            time.sleep(0.5)
        return element_s

class Check_toast(BaseView):

    def check_toast(self,toast):

        toast='//*[@text=\'{}\']'.format(toast)
        try:
            element_s=self.find_element_xpath(toast)
        except NoSuchElementException :
            logging.warring(" NoSuchElementException:%s"%toast)
            return False
        else:
            time.sleep(0.5)
            return element_s


class Save_screenshot(BaseView):

        def save_screenshot(self,imgname):
            try:
                self.save_screenshotimg(imgname)
            except Exception as e:
                logging.error('Savescreenshot error:\t', repr(e))
            else:
                logging.info('screenshot %s saved successfully'%imgname )

class Swipe_screen(BaseView):

    def swipe_screen(self,start_x,start_y,end_x,end_y):
        try:
            self.swipe_screenxy(start_x,start_y,end_x,end_y)
        except Exception:
            logging.warning('滑动失败，start_x:%s,start_y:%s,end_x:%s,end_y:%s'%(start_x,start_y,end_x,end_y))
        else:
            logging.info('滑动屏幕，start_x:%s,start_y:%s,end_x:%s,end_y:%s'%(start_x,start_y,end_x,end_y))












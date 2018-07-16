# -*- coding: utf-8 -*-
import os
import logging
import csv
from time import sleep,strftime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException

from common.baseView import BaseView
from selenium.webdriver.support.expected_conditions import *

# BaseView.save_screenshotimg()
class Common_func(BaseView):
    """
    公共类:
        check_element：查找元素，找到返回数据,找不到返回False，logging.warring
        check_element_xpath：查找元素（通过xpath），找到返回True,找不到返回False，logging.warring
        check_toast：查找飘窗，在一定时间内，每间隔多久查询一次数据
        save_screenshot :保存截屏，地址：/screenshots
        swipe_screen：页面滑动
        wait：等待
        long_wait：隐形等待，设置整个driver的最长等待时间
        get_csv_data：获取CSV数据
    """


    def check_element(self,element,name):
        try:
            elementtye=self.find_element(element)
        except NoSuchElementException as e:
            sleep(2) #为了输出log信息
            logging.warning('no element:%s'%name)
            return False
        else:
            return elementtye

    def check_element_xpath(self, element ,name):
        try:
            elementtye=self.find_element_xpath(element)
        except NoSuchElementException as e:
            sleep(2)
            logging.warning('no element:%s' % name)
            return False
        else:
            return elementtye

    def check_element_assess_id(self,element,name):
        try:
            elementtye=self.find_element_access_id(element)
        except NoSuchElementException as e:
            sleep(2) #为了输出log信息
            logging.warning('no element:%s'%name)
            return False
        else:
            return elementtye

    def check_toast(self,toast,time=5):
        """
        查找飘窗，在一定时间内，每间隔多久查询一次数据
        :param time: 超时时间
        :param interval:间隔时间
        :param toast:飘窗提示
        :return:True or False
        """
        toasttye='//*[@text=\'{}\']'.format(toast)
        try:
            elementtye=WebDriverWait(self.driver, 5, 0.5).until(lambda x:x.find_element_by_xpath(toasttye))
        except NoSuchElementException :
            sleep(2)
            logging.warring("NoSuchElementException:%s"%toast)
            return False
        else:
            return elementtye

    def getTime(self):
        now = strftime("%Y-%m-%d %H_%M_%S")
        return now

    def save_screenshot(self,imgname):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (imgname, time)
        try:
            self.save_screenshotimg(image_file)
        except Exception as e:
            logging.error('Savescreenshot error:\t', repr(e))
        else:
            logging.info('screenshot %s saved successfully'%imgname )

    def swipe_screen(self,start_x,start_y,end_x,end_y):
        try:
            self.swipe_screenxy(start_x,start_y,end_x,end_y)
        except Exception:
            logging.warning('滑动失败，start_x:%s,start_y:%s,end_x:%s,end_y:%s'%(start_x,start_y,end_x,end_y))
        else:
            logging.info('滑动屏幕，start_x:%s,start_y:%s,end_x:%s,end_y:%s'%(start_x,start_y,end_x,end_y))

    def wait(self,method,time=20,message=''):
        return WebDriverWait(self.driver, time,0.5).until(lambda x:method,message)

    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def check_viewstatus(self,viewname,method,message='',*args):
        logging.info('====check_%sStatus======'%viewname)
        try:
            len(args)
            method
        except (NoSuchElementException, TimeoutException):
            logging.error('%s Fail!'%message)
            self.save_screenshot('%s fail'%message)
            return False
        else:
            logging.info('%s success!'%message)
            return True














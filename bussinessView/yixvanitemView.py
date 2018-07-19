# -*- coding: utf-8 -*-
#已选项目页-派工
import logging
import time
from common.commonfunc import *
from basepage.yixvanitempage import Yixvanitem_page
from basepage.paigongpage import Paigong_page
from selenium.common.exceptions import NoSuchElementException,TimeoutException


class Yixvanitem(Yixvanitem_page,Paigong_page):

    sendview='new UiSelector().className("android.widget.TextView").text("派工")'

    def send(self):
        if self.yixvanitempage():
            sendtye=self.check_element(self.sendview,"派工")
            sendtye.click()

    def check_yixvanitemStatus(self):
        logging.info('====check_yixvanitemStatus======')
        try:
            # return WebDriverWait(self.driver, time).until(method,message)
            self.wait(self.paigongpage())
        except (NoSuchElementException, TimeoutException):
            logging.error('已选项目-派工 Fail!')
            self.save_screenshot('已选项目-派工 fail')
            return False
        else:
            logging.info('已选项目-派工 success!')
            return True

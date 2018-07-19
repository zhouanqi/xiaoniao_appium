# -*- coding: utf-8 -*-
#接车单电子档推送
import logging
import time
import json
from common.commonfunc import *
from basepage.jiechedanerweimapage import Jiechedanerweima_page
from basepage.yixvanitempage import Yixvanitem_page
from selenium.common.exceptions import NoSuchElementException,TimeoutException


# class Value:

class JcddianzidangView(Jiechedanerweima_page,Yixvanitem_page):


    yixvanitemview = 'new UiSelector().className("android.widget.FrameLayout").resourceId("com.hs.mywork.activity:id/btn2").index(4)'
    def yixvanitem(self):
        if self.jiechedanerweimapage():

            # print(type(self.yixvanitem))
            yixvanitemtye=self.check_element(self.yixvanitemview,"进入已选项目")
            # erweimapagetye = self.check_element(self.erweimapage, "接车单-电子档推送")
            yixvanitemtye.click()



    def check_jdcdianzidangStatus(self):
        logging.info('====check_dcdianzidangStatus======')
        try:
            self.wait(self.yixvanitempage())
        except (NoSuchElementException, TimeoutException):
            logging.error('接车单-已选项目 Fail!')
            self.save_screenshot('接车单-已选项目 fail')
            return False
        else:
            logging.info('接车单-已选项目 success!')
            return True
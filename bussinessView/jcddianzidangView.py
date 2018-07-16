# -*- coding: utf-8 -*-
#接车单电子档推送
import logging
import time
from common.commonfunc import *
from basepage.jiechedanerweimapage import Jiechedanerweima_page
from basepage.yixvanitempage import Yixvanitem_page
from selenium.common.exceptions import NoSuchElementException,TimeoutException


class JcddianzidangView(Jiechedanerweima_page,Yixvanitem_page):
    yixvanitem='new UiSelector().className("android.widget.TextView").text("进入已选项目")'
    # parts_tab = 'new UiSelector().resourceId("com.hs.mywork.activity:id/text1").text("配件")'

    def yixvanitem(self):
        if self.jiechedanerweimapage():
            # print(type(self.yixvanitem))
            yixvanitemtye=self.check_element(self.yixvanitem,"进入已选项目")
            # yixvanitemtye.click()


    def check_jdcdianzidangStatus(self):
        logging.info('====check_dcdianzidangStatus======')
        try:
            # return WebDriverWait(self.driver, time).until(method,message)
            self.wait(self.yixvanitempage())
        except (NoSuchElementException, TimeoutException):
            logging.error('接车单-已选项目 Fail!')
            self.save_screenshot('接车单-已选项目 fail')
            return False
        else:
            logging.info('接车单-已选项目 success!')
            return True
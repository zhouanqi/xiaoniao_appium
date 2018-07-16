# -*- coding: utf-8 -*-
#派工操作，默认第一个人派工
import logging
import time
from common.commonfunc import *

from basepage.fenpeijishipage import Fenpeijishi_page
from bussinessView.fenpaijishiView import FenpeijishiView
from selenium.common.exceptions import NoSuchElementException,TimeoutException


class PaigongView(FenpeijishiView,Fenpeijishi_page):

    fengpeijishi='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_sa").text("分配技师")'
    selete_all='new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").text("全选")'
    surejishi='new UiSelector().resourceId("android.widget.TextView").text("确认施工")'


    def paigong(self):
        if self.paigongpage():
            # selete_alltye=self.check_element(self.selete_all,'项目全选')
            # selete_alltye.click()


            fengpeijishitye=self.check_element(self.fengpeijishi,'分配技师按钮')
            fengpeijishitye.click()
            self.wait(self.check_element(self.fengpeijishi,'分配技师页面'),message="分配技师失败")

            self.chosejishi()
            logging.info("派工")

            surepaigongtye=self.check_element(self.surejishi,"确认施工")

            self.wait(self.check_toast('亲，派工已完成'),message="派工失败")

    def check_paigongStatus(self):
        logging.info('====check_paigongStatus======')
        try:

            self.paigong()
        except (NoSuchElementException, TimeoutException):
            logging.error('派工 Fail!')
            self.save_screenshot('派工 fail')
            return False
        else:
            logging.info('派工 success!')
            return True




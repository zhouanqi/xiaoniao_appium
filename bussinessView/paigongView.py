# -*- coding: utf-8 -*-
#派工操作，默认第一个人派工
import logging
import time
from common.commonfunc import *

from basepage.fenpeijishipage import Fenpeijishi_page
from bussinessView.fenpaijishiView import FenpeijishiView


class PaigongView(FenpeijishiView,Fenpeijishi_page,Check_toast):

    fengpeijishi='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_sa").text("分配技师")'
    selete_all='new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").text("全选")'
    surejishi='new UiSelector().resourceId("android.widget.TextView").text("确认施工")'


    def paigong(self):
        if self.paigongpage():
            # selete_alltye=self.check_element(self.selete_all,'项目全选')
            # selete_alltye.click()
            # self.wait(2)

            fengpeijishitye=self.check_element(self.fengpeijishi,'分配技师按钮')
            fengpeijishitye.click()
            self.wait(5).until(self.check_element(self.fengpeijishi,'分配技师页面'))

            self.chosejishi()

            logging.info("派工")

            surepaigongtye=self.check_element(self.surejishi,"确认施工")

            self.wait(5).until(Check_toast.check_toast('亲，派工已完成'))




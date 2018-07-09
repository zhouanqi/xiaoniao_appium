# -*- coding: utf-8 -*-
import time
import logging
from common.commonfunc import Check_func
class Paigong_page(Check_func):
    def paigongpage(self):
        #判断扫描接车图片确定首页
        paigong='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_title").text("派工")'

        paigongtye=self.check_element(paigong,"派工页")
        if paigongtye:
            return True
        else:
            return False
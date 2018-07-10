# -*- coding: utf-8 -*-
#派工页面
import time
import logging
from common.commonfunc import Common_func
class Paigong_page(Common_func):
    def paigongpage(self):
        #判断扫描接车图片确定首页
        paigong='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_title").text("派工")'

        paigongtye=self.check_element(paigong,"派工页")
        if paigongtye:
            return True
        else:
            return False
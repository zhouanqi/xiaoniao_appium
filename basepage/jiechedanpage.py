# -*- coding: utf-8 -*-
import time
import logging
from common.commonfunc import Check_func
class Jiechedan_page(Check_func):
    def jiecehdanpage(self):
        #判断扫描接车图片确定首页
        jiechedan='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_toolbar").text("接车单")'
        jiecehdanpage=self.check_element(jiechedan,"接车单页面")
        if jiecehdanpage:
            return True
        else:
            return False
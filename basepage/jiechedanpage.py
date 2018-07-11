# -*- coding: utf-8 -*-
import time
import logging
from common.commonfunc import Common_func
class Jiechedan_page(Common_func):
    """
    接车单页面，判断页面标题接车单
    """
    jiechedan = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_toolbar").text("接车单")'


    def jiecehdanpage(self):
        jiecehdanpage=self.check_element(self.jiechedan,"接车单页面")
        if jiecehdanpage:
            return True
        else:
            return False
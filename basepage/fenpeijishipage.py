# -*- coding: utf-8 -*-
import time
import logging
from common.commonfunc import Common_func

class Fenpeijishi_page(Common_func):
    fengpeijishi='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_toolbar").text("分配技师")'

    def fengpeijishi(self):
        fenpeijishitye=self.check_element(self.fengpeijishi,'分配技师页面')
        if fenpeijishitye:
            return True
        else:
            return False


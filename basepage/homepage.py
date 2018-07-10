# -*- coding: utf-8 -*-
import time
import logging
from common.commonfunc import Common_func
class Home_page(Common_func):
    """
    首页页面，判断扫描接车图片确定首页
    """
    saomianimg = 'new UiSelector().resourceId("com.hs.mywork.activity:id/imageView8").index(3)'


    def homepage(self):
        saomianimgtye=self.check_element(self.saomianimg,'首页')
        if saomianimgtye:
            return True
        else:
            return False
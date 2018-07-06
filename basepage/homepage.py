# -*- coding: utf-8 -*-
import time
import logging
from common.commonfunc import Check_func
class Home_page():
    def homepage(self):
        #判断扫描接车图片确定首页
        saomianimg='new UiSelector().resourceId("com.hs.mywork.activity:id/imageView8").index(3)'

        saomianimgtye=Check_func.check_element(saomianimg,'首页')
        if saomianimgtye:
            return True
        else:
            return False
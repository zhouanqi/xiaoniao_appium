# -*- coding: utf-8 -*-
import time
import logging
from common.commonfunc import Common_func
class Jiechedanerweima_page(Common_func):
    erweimapage = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_title").text("接车单")'
    def jiechedanerweimapage(self):
        #判断扫描接车图片确定首页
        erweimapagetye=self.check_element(self.erweimapage,'接车单-电子档推送')
        if erweimapagetye:
            return True
        else:
            return False
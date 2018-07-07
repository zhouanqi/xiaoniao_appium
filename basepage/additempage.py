# -*- coding: utf-8 -*-
import time
import logging
from common.commonfunc import Check_func
class Additem_page(Check_func):
    def additempage(self):
        #判断扫描接车图片确定首页
        additem='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_toolbar").text("添加项目")'

        additempage=self.check_element(additem,"添加项目页面")
        if additempage:
            return True
        else:
            return False

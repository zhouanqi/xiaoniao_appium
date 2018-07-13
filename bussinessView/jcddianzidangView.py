# -*- coding: utf-8 -*-
#接车单电子档推送
import logging
import time
from common.commonfunc import *
from basepage.jiechedanerweimapage import Jiechedanerweima_page

class JcddianzidangView(Jiechedanerweima_page):
    yixvanitem='new UiSelector().className("android.widget.TextView").text("进入已选项目")'
    # parts_tab = 'new UiSelector().resourceId("com.hs.mywork.activity:id/text1").text("配件")'

    def yixvanitem(self):
        if self.jiechedanerweimapage():
            # print(type(self.yixvanitem))
            yixvanitemtye=self.check_element(self.yixvanitem,"进入已选项目")
            # yixvanitemtye.click()



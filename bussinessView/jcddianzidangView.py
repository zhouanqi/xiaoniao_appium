# -*- coding: utf-8 -*-
import logging
import time
from common.commonfunc import *
from basepage.jiechedanerweimapage import Jiechedanerweima_page

class Jcddianzidang(Jiechedanerweima_page):
    yixvanitem='new UiSelector().className("android.widget.TextView").text("进入已选项目")'

    def jcderweima(self):
        return self.jiechedanerweimapage()

    def yixvanitem(self):
        yixvanitemtye=self.check_element(self.yixvanitem,'进入已选项目')
        yixvanitemtye.click()
        time.sleep(2)


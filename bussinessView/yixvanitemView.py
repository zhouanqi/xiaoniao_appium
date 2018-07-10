# -*- coding: utf-8 -*-
#已选项目页-派工
import logging
import time
from common.commonfunc import *
from basepage.yixvanitempage import Yixvanitem_page

class Yixvanitem(Yixvanitem_page):

    send='new UiSelector().resourceId("com.hs.mywork.activity:id/loading_tech").text("派工")'
    def send(self):
        if self.yixvanitempage():
            sendtye=self.check_element(self.send,"派工")
            sendtye.click()
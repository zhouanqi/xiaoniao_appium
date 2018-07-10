# -*- coding: utf-8 -*-
import logging
import time
from common.commonfunc import *
from basepage.fenpeijishipage import Fenpeijishi_page
from basepage.paigongpage import Paigong_page

class FenpeijishiView(Fenpeijishi_page,Paigong_page):

    jishi = 'new UiSelector().resourceId("com.hs.mywork.activity:id/imageView").index(2)'

    def chosejishi(self):
        if self.fengpeijishi():
            jishitye=self.check_element(self.jishi,'选择技师,默认第一个')
            jishitye.click()
            logging.info("分配技师")

            self.wait(5).until(self.paigongpage())



# -*- coding: utf-8 -*-
# import logging
#
# import os
# from os import path
# import logging.config
# from config.appium_config import appium_desired
import time
import logging
from common.commonfunc import Check_func


class JiecheView(Check_func):

    def jieche_action(self, carno):

        time.sleep(2)
        logging.info('接车carno:%s  '%carno)
        carno_weizhi='new UiSelector().className("android.widget.TextView").instance(7)'
        carno_weizhitye=self.check_element(carno_weizhi,'首页输出车牌框')

        carno_weizhitye.click()
        time.sleep(1)

        for i in range(len(carno)):
            carname='carno_'+str(i)
            carname='new UiSelector().className("android.widget.TextView").text("'+carno[i]+'")'
            carname_tye=self.check_element(carname,str(carname))
            carname_tye.click()
            time.sleep(0.5)
        go_tye=self.check_element('new UiSelector().className("android.widget.TextView").text("GO")','carno_go')
        go_tye.click()
        time.sleep(0.5)

        sure_tye=self.check_element('new UiSelector().className("android.widget.Button").text("确定")','carno_sure')
        sure_tye.click()
        time.sleep(0.5)


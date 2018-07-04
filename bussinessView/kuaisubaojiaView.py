# -*- coding: utf-8 -*-
import logging
from common.commonfunc import Check_func
import os
from os import path
import logging.config
from config.appium_config import appium_desired


class JiecheView(Check_func):

    def jieche_action(self, carno):

        carno_weizhi='new UiSelector().className("android.widget.TextView").index(0)'
        carno_weizhitye=self.check_element(carno_weizhi)
        carno_weizhitye.click()
        for i in range(len(carno)):
            carname='carno_'+str(i)
            carname='new UiSelector().className("android.widget.TextView").text("'+carno[i]+'")'
            logging.info(carname)
            carname_tye=self.check_element(carname)

            carname_tye.click()
#                                             new UiSelector().className("android.widget.TextView").text("粤")
# driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").index(0)').click()
# #选择车牌号
# carno_yue=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("粤")').click()
# carno_A=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("A")').click()
# carno_eight=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("8")')
# carno_eight.click()
# carno_eight.click()
# carno_night=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("9")')
# carno_night.click()
# carno_night.click()
# carno_one=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("1")').click()
# carno_GO=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("GO")').click()
# quedingbutton=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").text("确定")').click()
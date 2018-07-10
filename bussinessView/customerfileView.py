# -*- coding: utf-8 -*-
import time
from common.commonfunc import *

class CustomerfileView(Common_func):
    """
    客户档案，如果有订单-继续下单
    填写里程和油量信息
    """
    continuetye = 'new UiSelector().resourceId("com.hs.mywork.activity:id/txt_title").index(0)'
    continue_order = 'new UiSelector().className("android.widget.TextView").text("继续下单")'
    milleage = 'new UiSelector().resourceId("com.hs.mywork.activity:id/et_distance")'
    oil = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_oil")'
    oilF = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_item")'

    def continueorder(self):

        if self.check_element(self.continuetye,'继续下单选项框'):
            #如果有订单信息,点击继续下单
            continue_order=self.check_element(self.continue_order,'继续下单')
            continue_order.click()
        else:
            pass

    def modifyinfor(self, milleagenum):
        """
        填写基础信息
        :param milleagenum: 里程

        """
        mileagetye=self.check_element(self.milleage,'本次来场里程')
        mileagetye.send_keys(milleagenum)
        self.wait(0.5)

        self.swipe_screen(0.3, 0.7, 0.3, 0.1)

        oiltye=self.check_element(self.oil,'油量')
        oiltye.click()
        self.wait(0.5)

        oilFtye=self.check_element(self.oilF,'油量F')
        oilFtye.click()
        self.wait(0.5)




#
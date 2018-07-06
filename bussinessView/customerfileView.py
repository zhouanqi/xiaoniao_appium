# -*- coding: utf-8 -*-
import time
from common.commonfunc import Check_func

class CustomerfileView(Check_func):

    def continueorder(self):

        continuetye='new UiSelector().resourceId("com.hs.mywork.activity:id/txt_title").index(0)'
        continue_order='new UiSelector().className("android.widget.TextView").text("继续下单")'

        if self.check_element(continuetye,'继续下单选项框'):
            #如果有订单信息,点击继续下单
            continue_order=self.check_element(continue_order,'继续下单')
            continue_order.click()
        else:
            pass

    def modifyinfor(self, milleagenum):

        milleage='new UiSelector().resourceId("com.hs.mywork.activity:id/et_distance")'
        oil='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_oil")'
        oilF='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_item")'

        mileagetye=self.check_element(milleage,'本次来场里程')
        oiltye=self.check_element(oil,'油量')

        mileagetye.send_keys(milleagenum)
        time.sleep(0.5)
        oiltye.click()
        time.sleep(0.5)

        oilFtye=self.check_element(oilF,'油量F')
        oilFtye.click()
        time.sleep(0.5)

    def quickquote(self):
        pass


#
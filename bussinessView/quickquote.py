# -*- coding: utf-8 -*-
import logging
import time
from common.commonfunc import *
class Quickquote(Check_func,Swipe_screen):

    def quick_quote(self,start_x,start_y,end_x,end_y):
        #滑动到快速报价
        self.swipe_screenxy(start_x,start_y,end_x,end_y)
        time.sleep(0.5)
        #点击快速报价
        quote='new UiSelector().resourceId("com.hs.mywork.activity:id/tv_quote").text("快速报价")'
        quote=self.check_element(quote,'快速报价')
        time.sleep(0.5)
        quote.click()
        #选择维修类型-普通
        normal='new UiSelector().resourceId("com.hs.mywork.activity:id/putong").text("普通")'
        normal.self.check_element(normal,'普通维修')
        normal.click()

    def add_item(self):
        pass
        # driver.swipe(start_x=mobile_x * 0.3, start_y=mobile_y * 0.99, end_x=mobile_x * 0.3, end_y=mobile_y * 0.1,
        #              duration=2000)
        # logging.info(start_x=mobile_x*0.3, start_y=mobile_y*0.99, end_x=mobile_x*0.3, end_y=mobile_y*0.1)
        # driver.implicitly_wait(10)
        # #
        # driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").resourceId("com.hs.mywork.activity:id/tv_name").text("保养套餐")').click()
        # driver.implicitly_wait(2)
        # try:
        #     baoyang_package=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.hs.mywork.activity:id/check_box").index(0)')
        # except NoSuchElementException:
        #     logging.info("没有快速报价，添加保养套餐元素")
        # else:
        #     baoyang_package.click()

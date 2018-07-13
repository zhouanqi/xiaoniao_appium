# -*- coding: utf-8 -*-
import time
from common.commonfunc import *
from selenium.common.exceptions import NoSuchElementException,TimeoutException

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
    #快速报价
    quote = 'new UiSelector().resourceId("com.hs.mywork.activity:id/tv_quote").text("快速报价")'
    normal = 'new UiSelector().resourceId("com.hs.mywork.activity:id/putong").text("普通")'
    normalitem='new UiSelector().resourceId("com.hs.mywork.activity:id/tab_text").text("常规项目")'


    def continueorder(self):

        self.wait(self.check_element(self.continuetye,'继续下单选项框'))
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

        self.swipe_screen(0.3, 0.7, 0.3, 0.1)

        oiltye=self.check_element(self.oil,'油量')
        oiltye.click()

        oilFtye=self.check_element(self.oilF,'油量F')
        oilFtye.click()

    def quick_quote(self):
        # 滑动到快速报价
        self.swipe_screenxy(0.08, 0.7, 0.3, 0.3)
        # 点击快速报价
        quote = self.check_element(self.quote, '快速报价')
        quote.click()
        self.check_toast('客户信息保存成功')
        # 选择维修类型-普通
        normal = self.wait(self.check_element(self.normal, '普通维修'))
        normal.click()

        self.check_toast("报价成功")

    def swipebottom_page(self):
        jiechedantye = False
        while jiechedantye == False:
            logging.info("----------------------------------")
            self.swipe_screen(0.08, 0.7, 0.3, 0.3)
            jiechedantye = self.check_element(self.quote, '快速报价')
        return jiechedantye

    #验证
    def check_jiecheStatus(self):
        #滑动，找到
        self.swipe_screen(0.08, 0.7, 0.3, 0.3)

        try:
            # return WebDriverWait(self.driver, time).until(method,message)
            normalitem = self.wait(self.check_element(self.normalitem), "报价-常规项目")
        except (NoSuchElementException, TimeoutException):
            logging.error('客户档案报价 Fail!')
            self.save_screenshot('客户档案报价 fail')
            return False
        else:
            logging.info('接客户档案报价 success!')
            return True

#
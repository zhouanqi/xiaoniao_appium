# -*- coding: utf-8 -*-

import logging
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from common.commonfunc import Common_func
from basepage.kehudanganpage import Kehudangan_page

class JiecheView(Kehudangan_page):
    """
    首页输入车牌接车
    """
    carno_weizhi = 'new UiSelector().className("android.widget.TextView")'
    carno_weizhi_xpath = '//android.widget.LinearLayout[@className="android.widget.TextView" and index=6]'
    go_butt='new UiSelector().className("android.widget.TextView").text("GO")'
    sure_butt='new UiSelector().className("android.widget.Button").text("确定")'

    def jieche_action(self, carno):

        logging.info('接车carno:%s  '%carno)
        #定位首页车牌输入框
        self.check_element('new UiSelector().resourceId("com.hs.mywork.activity:id/editText5").index(0)',"首页车牌框整体")
        for i in range(7):
            carno_weizhi=self.carno_weizhi+".index("+str(i)+")"
            carno_weizhitye=self.check_element(carno_weizhi, '首页车牌输入框：%s'%i)
            if carno_weizhitye:
                carno_weizhitye.click()
                break


        for i in range(len(carno)):
            carname='carno_'+str(i)
            carname='new UiSelector().className("android.widget.TextView").text("'+carno[i]+'")'
            carname_tye=self.check_element(carname,str(carname))
            carname_tye.click()

        go_tye=self.check_element(self.go_butt,'carno_go')
        go_tye.click()

        sure_tye=self.check_element(self.sure_butt,'carno_sure')
        sure_tye.click()

    def check_jiecheStatus(self):
        logging.info('====check_jiehceStatus======')
        try:
            self.wait(self.kehudanganpage(),message="接车没有找到客户档案页")
        except (NoSuchElementException, TimeoutException):
            logging.error('接车 Fail!')
            self.save_screenshot('接车 fail')
            return False
        else:
            logging.info('接车 success!')
            return True


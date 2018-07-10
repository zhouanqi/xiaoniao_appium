# -*- coding: utf-8 -*-

import logging
from common.commonfunc import Common_func


class JiecheView(Common_func):
    """
    首页输入车牌接车
    """
    carno_weizhi = 'new UiSelector().className("android.widget.TextView").instance(11)'
    go_butt='new UiSelector().className("android.widget.TextView").text("GO")'
    sure_butt='new UiSelector().className("android.widget.Button").text("确定")'

    def jieche_action(self, carno):
        self.wait(10)
        logging.info('接车carno:%s  '%carno)

        carno_weizhitye = self.check_element(self.carno_weizhi, '首页输入车牌框')
        self.wait(2)

        carno_weizhitye.click()
        self.wait(1)

        for i in range(len(carno)):
            carname='carno_'+str(i)
            carname='new UiSelector().className("android.widget.TextView").text("'+carno[i]+'")'
            carname_tye=self.check_element(carname,str(carname))
            carname_tye.click()
            self.wait(0.5)

        go_tye=self.check_element(self.go_butt,'carno_go')
        go_tye.click()
        self.wait(0.5)

        sure_tye=self.check_element(self.sure_butt,'carno_sure')
        sure_tye.click()
        self.wait(0.5)


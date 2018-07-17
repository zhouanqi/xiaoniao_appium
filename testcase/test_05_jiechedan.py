# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.jiechedanView import JiechedanView

class TestJiechedan(StartEnd):
     """
     接车单用例：
          创建接车单，全选车辆能内部，全选随车装备，点击电子档推送
     判断是否进入到接车单页面
     """

     def test_jiechedan_01(self):
        logging.info('============test_jiechedan_01================')
        J = JiechedanView(self.driver)
        J.quickquote_jiechedan()
        J.carinternal_seleteall()
        J.suichezhaungbei_seleteall()
        # 电子档推送
        J.dianzidangtuisong()
        self.assertTrue(J.check_jiechedanStatus())


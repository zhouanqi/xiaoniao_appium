# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.jiechedanView import JiechedanView

class TestJiechedan(StartEnd):

   def test_jiechedan_01(self):
        logging.info('============test_jiechedan_01================')
        J = JiechedanView(self.driver)
        J.quickquote_jiechedan()
        J.carinternal_seleteall()
        J.suichezhaungbei_seleteall()
        # 电子档推送
        J.dianzidangtuisong()
        self.assertTrue(J.check_jiechedanStatus())


# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.customerfileView import CustomerfileView

class TestKuhudangan_baojia(StartEnd):

   def test_kehudangan_baojia_01(self):
        logging.info('============test_kehudangan_baojia_01================')
        C=CustomerfileView(self.driver)
        #是否已有工单
        C.continueorder()
        #修改客户信息
        C.modifyinfor('87654')
        #快速报价
        C.quick_quote()
        self.assertTrue(C.check_customerbaojiaStatus())
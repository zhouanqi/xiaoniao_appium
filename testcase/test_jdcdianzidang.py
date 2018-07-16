# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.jcddianzidangView import JcddianzidangView

class TestJdcdianzidang(StartEnd):

   def test_jdcdianzidang_01(self):
        logging.info('============test_jdcdianzidang_01================')
        J = JcddianzidangView(self.driver)
        J.yixvanitem()
        self.assertTrue(J.check_jdcdianzidangStatus())


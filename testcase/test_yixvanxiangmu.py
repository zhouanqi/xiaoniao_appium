# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.yixvanitemView import Yixvanitem

class TestJieche(StartEnd):

   def test_jieche_01(self):
        logging.info('============test_jieche_01================')
        Y=Yixvanitem(self.driver)
        Y.send()
        self.assertTrue(Y.check_yixvanitemStatus())


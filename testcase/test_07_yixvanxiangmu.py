# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.yixvanitemView import Yixvanitem

class TestYixvanxiangmu(StartEnd):

   def test_yixvanxiangmu_01(self):
        logging.info('============test_yixvanxiangmu_01================')
        Y=Yixvanitem(self.driver)
        Y.send()
        self.assertTrue(Y.check_yixvanitemStatus())


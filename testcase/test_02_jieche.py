# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.jiecheView import JiecheView

class TestJieche(StartEnd):

   def test_jieche_01(self):
        logging.info('============test_jieche_01================')
        j=JiecheView(self.driver)
        j.jieche_action('粤A88991')
        self.assertTrue(j.check_jiecheStatus())


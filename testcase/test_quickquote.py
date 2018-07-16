# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.quickquoteView import QuickquoteView

class TestQuickquote(StartEnd):

   def test_quickquote_01(self):
        logging.info('============test_quickquote_01================')
        Q = QuickquoteView(self.driver)
        self.assertTrue(Q.check_quickquoteStatus())


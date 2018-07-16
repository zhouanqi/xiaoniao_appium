# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.paigongView import PaigongView

class TestPaigong(StartEnd):

   def test_quickquotepaigong_01(self):
        logging.info('============test_quickquote_01================')
        P = PaigongView(self.driver)
        self.assertTrue(P.check_paigongStatus())


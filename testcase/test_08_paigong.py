# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.paigongView import PaigongView

class TestPaigong(StartEnd):
    """
        点击分配技师,查找分配技师页面,选择一个技师派工,点击确认施工
    """
    def test_paigong_01(self):
        logging.info('============test_paigong_01================')
        P = PaigongView(self.driver)
        self.assertTrue(P.check_paigongStatus())


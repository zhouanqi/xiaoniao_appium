# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.jcddianzidangView import JcddianzidangView

class TestJdcdianzidang(StartEnd):
    """
        由接车单进入已选项目页面，判断是否进入已选项目
    """
    def test_jdcdianzidang_01(self):
        logging.info('============test_jdcdianzidang_01================')
        J = JcddianzidangView(self.driver)
        J.yixvanitem()
        self.assertTrue(J.check_jdcdianzidangStatus())


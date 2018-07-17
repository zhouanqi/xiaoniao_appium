# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.quickquoteView import QuickquoteView

class TestQuickquote(StartEnd):
    """
    快速报价：
        选择普通维修，默认第一个保养套餐，第一个工时项目，第一个配件项目，第一个喷漆项目，无订单和活动
        如若出现找不到元素或者是超时则失败
    """

    def test_quickquote_01(self):
        logging.info('============test_quickquote_01================')
        Q = QuickquoteView(self.driver)
        self.assertTrue(Q.check_quickquoteStatus())


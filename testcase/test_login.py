# -*- coding: utf-8 -*-
import unittest2
import logging
from common.startend import StartEnd
from bussinessView.loginView import LoginView

class TestLogin(StartEnd):

   def test_login_01(self):
        logging.info('============test_login_01================')
        L=LoginView(self.driver)
        longnot = L.loginin_not()
        if longnot == False:
            # 如果有登录页面（无进入首页）,登录
            logging.info("logging start")
            self.assertTrue(L.check_loginStatus('027310', '1'))


   @unittest2.skip('test_login_error')
   def test_login_error(self):
       logging.info('==============test_login_error==============')
       l = LoginView(self.driver)

       longnot = l.loginin_not()
       if longnot == False:
           # 如果有登录页面（无进入首页）,登录
           logging.info("logging start")
           l.login_action('027310', '8')
       self.assertTrue(l.check_loginStatus(),msg='login fail!')



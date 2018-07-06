# -*- coding: utf-8 -*-

import os
from os import path
import logging.config
from config.appium_config import *

from bussinessView.loginView import LoginView
from bussinessView.jiecheView import JiecheView
from bussinessView.customerfileView import CustomerfileView
from bussinessView.quickquote import Quickquote

log_file_path = os.path.join('..\config', 'log.config')
# print(log_file_path)
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logging=logging.getLogger()


if __name__=='__main__':
    driver = appium_desired()

    #登录
    l=LoginView(driver)
    if l.loginin_not is False:
        #如果有登录页面（无进入首页）,登录
        l.login_action('027310','81')

    #首页-接车
    j=JiecheView(driver)
    j.jieche_action('粤A88991')

    #客户档案
    C=CustomerfileView(driver)
    #是否已有工单
    C.continueorder()
    #修改客户信息
    C.modifyinfor('87654')

    Q=Quickquote(driver)
    Q.quick_quote(0.3, 0.99, 0.3, 0.1)





# -*- coding: utf-8 -*-

import logging.config
from common.appium_config import *

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
    longnot=l.loginin_not()
    if longnot ==False:

        #如果有登录页面（无进入首页）,登录
        logging.info("logging start")
        l.login_action('027310','1')

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
    Q.add_pack_item()
    Q.backhome()
    Q.add_workh_item()
    Q.backhome()





# -*- coding: utf-8 -*-
import unittest2
import logging.config
from common.appium_config import *

from bussinessView.loginView import LoginView
from bussinessView.jiecheView import JiecheView
from bussinessView.customerfileView import CustomerfileView
from bussinessView.quickquoteView import QuickquoteView
from bussinessView.jiechedanView import JiechedanView
from bussinessView.jcddianzidangView import JcddianzidangView
from bussinessView.yixvanitemView import Yixvanitem
from bussinessView.paigongView import PaigongView
from testcase.test_login import TestLogin

log_file_path = os.path.join('..\config', 'log.config')
# print(log_file_path)
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logging=logging.getLogger()


if __name__=='__main__':


    #登录

    driver.implicitly_wait(5)
    unittest2.main()
    # l=LoginView(driver)
    # longnot=l.loginin_not()
    # if longnot ==False:
    #     #如果有登录页面（无进入首页）,登录
    #     logging.info("logging start")
    #     l.login_action('027310','1')

    #首页-接车
    # j=JiecheView(driver)
    # j.jieche_action('粤A88991')
    # #
    # #客户档案
    # C=CustomerfileView(driver)
    # #是否已有工单
    # C.continueorder()
    # #修改客户信息
    # C.modifyinfor('87654')
    #
    # #快速报价
    # Q=QuickquoteView(driver)
    # Q.quick_quote()
    # Q.add_pack_item()
    # Q.backhome()
    # Q.add_workh_item()
    # Q.backhome()
    # Q.add_parts_item()
    # Q.backhome()
    # Q.add_spraypaint_item()
    # Q.backhome()
    # #
    # #创建接车单
    # jiecehdan=JiechedanView(driver)
    # jiecehdan.quickquote_jiechedan()
    # jiecehdan.carinternal_seleteall()
    # jiecehdan.suichezhaungbei_seleteall()
    # #电子档推送
    # jiecehdan.dianzidangtuisong()
    # #
    # #接车单电子档页面-已选项目
    # jcddianzidang=JcddianzidangView(driver)
    # jcddianzidang.jcderweima()
    # jcddianzidang.yixvanitem()
    # #
    # #已选项目-派工
    # jdcyixvanitem=Yixvanitem(driver)
    # jdcyixvanitem.send()
    #
    # 派工
    # paigong=PaigongView(driver)
    # paigong.paigong()



# -*- coding: utf-8 -*-
import logging
from common.commonfunc import Check_func
import os
from os import path
import logging.config
from config.appium_config import appium_desired


class LoginView(Check_func):


    def loginin_not(self):

        carno_weizhi=self.find_element('new UiSelector().className("android.widget.TextView").index(0)')
        if carno_weizhi:
            return False
        else:
            return True

    def login_action(self,loginname,password):

        loginname_type = 'new UiSelector().text("请输入用户名")'
        password_type = 'new UiSelector().className("android.widget.EditText").resourceId("com.hs.mywork.activity:id/iev_pwd")'
        loginin_type = 'new UiSelector().className("android.widget.FrameLayout").resourceId("com.hs.mywork.activity:id/btn_login")'

        tyename=self.check_element(loginname_type)
        tyepas=self.check_element(password_type)
        tyein=self.check_element(loginin_type)

        logging.info('loginname:%s,password:%s' %(loginname,password))
        tyename.send_keys(loginname)
        tyepas.send_keys(password)
        tyein.click()
        logging.info('login is worked  ')





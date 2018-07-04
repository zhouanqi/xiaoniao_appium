# -*- coding: utf-8 -*-
import logging
from common.commonfunc import Login_func
import os
from os import path
import logging.config
from config.appium_config import appium_desired


class LoginView(Login_func):

    def login_action(self,loginname,password):

        loginname_type = ('new UiSelector().text("请输入用户名")')

        password_type = (
        'new UiSelector().className("android.widget.EditText").resourceId("com.hs.mywork.activity:id/iev_pwd")')

        loginin_type = (
        'new UiSelector().className("android.widget.FrameLayout").resourceId("com.hs.mywork.activity:id/btn_login")')

        tyename=self.check_element(loginname_type)
        tyepas=self.check_element(password_type)
        tyein=self.check_element(loginin_type)

        logging.info('loginname:%s,password:%s' %(loginname,password))
        tyename.send_keys(loginname)
        tyepas.send_keys(password)
        tyein.click()
        logging.info('login is worked  ')





if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('027310','1')



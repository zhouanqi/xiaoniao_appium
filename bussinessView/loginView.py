# -*- coding: utf-8 -*-
import logging
import time
from common.commonfunc import *
from basepage.homepage import Home_page


class LoginView(Check_toast,Home_page):

    def loginin_not(self):
        time.sleep(10)
        #如果页面为首页，则不需要登录
        homepage=self.homepage()
        print('homepage',homepage)
        return homepage

    def login_action(self,loginname,password):

        time.sleep(2)
        loginname_type = 'new UiSelector().resourceId("com.hs.mywork.activity:id/iev_user").index(1)'
        password_type = 'new UiSelector().className("android.widget.EditText").resourceId("com.hs.mywork.activity:id/iev_pwd")'
        loginin_type = 'new UiSelector().className("android.widget.FrameLayout").resourceId("com.hs.mywork.activity:id/btn_login")'

        tyename=self.check_element(loginname_type,'loginname')
        tyepas=self.check_element(password_type,'password')
        tyein=self.check_element(loginin_type,'login_button')

        logging.info('loginname:%s,password:%s' %(loginname,password))
        time.sleep(0.5)
        tyename.send_keys(loginname)
        time.sleep(0.5)
        tyepas.send_keys(password)
        time.sleep(0.5)
        tyein.click()

               # try:
        #     tast_element = time.sleep(5).until(self.check_toast('登录成功'))
        #     paserror=self.check_toast('登录失败,请检查用户信息')
        #     loginerror=self.check_toast('未知错误' )

        # if self.check_toast('登录失败,请检查用户信息'):
        #     logging.error('登录失败,请检查用户信息')
        # elif self.check_toast('未知错误' ):
        #     logging.error('未知错误')
        # elif self.homepage():
        #     tast_element=time.sleep(5).until(self.check_toast('登录成功'))
        #     logging.info('Login successfully  ')

       
        





# -*- coding: utf-8 -*-
import logging
import time
from basepage.homepage import Home_page


class LoginView(Home_page):
    """
    登录流程
    """
    #用户名
    loginname_type = 'new UiSelector().className("android.widget.EditText").resourceId("com.hs.mywork.activity:id/iev_user")'
    #密码
    password_type = 'new UiSelector().className("android.widget.EditText").resourceId("com.hs.mywork.activity:id/iev_pwd")'
    #登录按钮
    loginin_type = 'new UiSelector().className("android.widget.FrameLayout").resourceId("com.hs.mywork.activity:id/btn_login")'

    def loginin_not(self):
        """
        判断APP是否已经有登陆信息：跳过登录页面直接进入首页，
            能更直接找到首页，则为已登录
        :return:是否找到首页
        """
        self.wait(10) #等待程序执行进入首页
        return self.homepage()

    def login_action(self,loginname,password):
        #登录

        tyename=self.check_element(self.loginname_type,'loginname')
        tyepas=self.check_element(self.password_type,'password')
        tyein=self.check_element(self.loginin_type,'login_button')

        logging.info('loginname:%s,password:%s' %(loginname,password))

        tyename.send_keys(loginname)
        self.wait(2)
        tyepas.send_keys(password)
        self.wait(2)
        tyein.click()

        tast_element = self.check_toast('登录成功')
        paserror=self.check_toast('登录失败,请检查用户信息')
        if paserror:
            logging.error('登录失败,请检查用户信息')
        elif self.homepage():
            tast_element=self.check_toast('登录成功')
            logging.info('Login successfully  ')

       
        





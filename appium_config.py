# -*- coding: utf-8 -*-
import os
import yaml
from appium import webdriver


#配置文件
class Appium_sedired:
    """
    封装APP启动
    """
    def appium_desired(self):
        """
        appium启动设置

        :return:driver
        """
        # driver=webdriver.WebElement
        # try:
        #     driver.isAppInstalled('com.hs.mywork.activity')
        # expect
        with open('./desired_caps.yaml','r') as f:
            data=yaml.load(f)
        desired_caps={}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        desired_caps['noReset']=data['noReset']
        desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
        desired_caps['resetKeyboard']=data['resetKeyboard']
        driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
        driver.implicitly_wait(2)

        return driver


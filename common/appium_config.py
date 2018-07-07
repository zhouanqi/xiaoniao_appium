# -*- coding: utf-8 -*-
import os
import yaml
from appium import webdriver


# appium启动设置

def appium_desired():

    with open('E:\\jiaobenmanage\\3.6\\xiaoniao_appium\\config\\desired_caps_meizu.yaml','r') as f:
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
    desired_caps['automationName']=data['automationName']
    #真机
    desired_caps['udid'] = data['udid']
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(2)

    return driver


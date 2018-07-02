# -*- coding: utf-8 -*-
import os
import yaml
import logging.config
from appium import webdriver
#配置文件
class Appium_sedired:
    with open('//.desired_caps.yaml','r') as f:
        data=yaml.load(f)

    desired_caps={}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset']=data['noReset']
    desired_caps['noReset']=data['noReset']


    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(2)

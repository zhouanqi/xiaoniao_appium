# -*- coding: utf-8 -*-

import os
from os import path
import logging.config
from config.appium_config import *
from bussinessView.loginView import LoginView
from bussinessView.kuaisubaojiaView import JiecheView

log_file_path = os.path.join('..\config', 'log.config')
# print(log_file_path)
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logging=logging.getLogger()


if __name__=='__main__':
    driver = appium_desired()
    l=LoginView(driver)
    if l.loginin_not is True:
        print(l.loginin_not)
        l.login_action('027310','1')
    j=JiecheView(driver)
    j.jieche_action('粤A88991')





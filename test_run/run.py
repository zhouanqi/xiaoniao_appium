# -*- coding: utf-8 -*-
import os
import unittest2
from  BSTestRunner import BSTestRunner
import time
import logging.config
import sys

path='E:\\jiaobenmanage\\3.6\\xiaoniao_appium\\'
sys.path.append(path)

test_dir='../testcase'
report_dir='../reports'

#log
log_file_path = os.path.join('..\config', 'log.config')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logging=logging.getLogger()
discover=unittest2.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title='晓鸟 Test Report',description='晓鸟 Android app test report')
    logging.info('start run test case...')
    runner.run(discover)
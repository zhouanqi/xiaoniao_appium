# -*- coding: utf-8 -*-
import unittest2
from  BSTestRunner import BSTestRunner
import time,logging
import sys

path='E:\\jiaobenmanage\\3.6\\xiaoniao_appium\\'
sys.path.append(path)

test_dir='../testcase'
report_dir='../reports'

discover=unittest2.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title='Kyb Test Report',description='kyb Android app test report')
    logging.info('start run test case...')
    runner.run(discover)
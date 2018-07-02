# -*- coding: utf-8 -*-
import os
import logging

#获得当前的路径
FILE = os.getcwd()
# os.path.join 将多个路径组合后返回
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(FILE, 'log.txt'),
                    filemode='w')

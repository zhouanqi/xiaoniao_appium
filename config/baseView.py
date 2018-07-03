# -*- coding: utf-8 -*-

import os
from os import path
import logging
import logging.config
from appium_config import Appium_sedired


log_file_path = os.path.join(path.dirname(path.abspath(__file__)), 'log.config')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logging=logging.getLogger()


if __name__=='__main__':

    appium=Appium_sedired()
    appium.appium_desired()
    logging.info('app start')



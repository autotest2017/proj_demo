#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import logging
import unittest
from lib.Logger import Logger
from testcase.login_test_module import UTExample1

#logger = logging.getLogger("test")
#
#logger.setLevel(logging.DEBUG)#  这里有问题，没有设置成功日志级别。
#
#logging.error("this is an error message")
#logging.warn("warn message")
#logging.info("this is a info message")
#logging.debug("this is a debug message")
#
#FORMAT = "%(asctime)-15s %(clientip)s %(user)-8s %(message)s"
#logging.basicConfig(format=FORMAT)
#
#d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
#logging.warning("Protocol problem: %s", "connection reset", extra=d)


if __name__ == "__main__":
	logger = Logger().getlog()
	logger.info('start testcase...')
	
	suite = unittest.TestSuite()
	loader = unittest.TestLoader()
	suite.addTests(loader.loadTestsFromTestCase(UTExample1))
	unittest.TextTestRunner(verbosity=2).run(suite)
	
	logger.info('stop testcase...')
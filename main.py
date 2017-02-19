#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import time
import logging
import unittest
from lib.Logger import Logger
from lib.HTMLTestRunner import HTMLTestRunner
from testcase.admin_login_logout.admin_login_correction import AdminLoginCorrection
from testcase.admin_login_logout.admin_login_failure import AdminLoginFail

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(AdminLoginCorrection))
    suite.addTests(loader.loadTestsFromTestCase(AdminLoginFail))
    return suite

if __name__ == "__main__":
    logger = Logger().getlog()
    logger.info('start testcase...')

    fp = open('./result/test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'测试报告生成范例',
                            description=u"测试用例执行情况：")
    runner.run(suite())
    fp.close()

    logger.info('stop testcase...')
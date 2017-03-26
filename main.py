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
from lib.sendmail import send_email

FROM_ADDR = u"zelin_test@163.com"
FROM_PSWD = u"Zelin123456"  # 163设置的第三方授权码
TO_ADDR = u"zelin_test@163.com"


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(AdminLoginCorrection))
    suite.addTests(loader.loadTestsFromTestCase(AdminLoginFail))
    return suite

if __name__ == "__main__":
    logger = Logger().getlog()
    logger.info('start testcase...')
    report_path = './result/test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S")
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'测试报告生成范例',
                            description=u"测试用例执行情况：")
    runner.run(suite())
    fp.close()
    #send_email(dict, mode='html')
    send_email(FROM_ADDR, FROM_PSWD, TO_ADDR, u"冒烟测试报告", report_path)
    logger.info('stop testcase...')
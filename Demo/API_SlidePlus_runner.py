#coding=utf-8
#导入测试用例
import a_SNS_login
#加载unittest模块
import unittest
import time
#加载HTMLTestRunner，用于生成HTML result
import HTMLTestRunner

def run_api_Tests():       #定义执行测试用例及执行顺序
    suite = unittest.TestSuite()
    suite.addTest(a_SNS_login.SP_login("test_api_aa"))
    suite.addTest(a_SNS_login.SP_login("test_api_ac"))
    suite.addTest(a_SNS_login.SP_login("test_api_uc"))
    suite.addTest(a_SNS_login.SP_login("test_api_ad"))
    return suite

if __name__ == '__main__':
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    filename = "F:\\API_python\\Report\\report_" + now_time + ".html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='SlidePlus API 测试结果',
        description='报告详情如下：'
    )
    i = 1
    while i <= 5:
        suite = run_api_Tests()
        runner.run(suite)
        i = i + 1
    else:
        print("Test OK")
    fp.close()

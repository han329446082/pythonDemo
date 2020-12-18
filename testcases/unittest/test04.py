import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

import os

from __builtin__ import file


class TestTest(unittest.TestCase):
    """ 测试HTMLTestRunner """
    def test_b(self):
        print('aaaa')
        report_title = 'Example用例执行报告'
        desc = '用于展示修改样式后的HTMLTestRunner'
        report_file = 'aaa.html'
        testsuite = unittest.TestSuite()
        path = os.path.dirname(os.path.abspath(__file__))
        testsuite.addTest( unittest.TestLoader().discover(path))

        with open(report_file, 'wb') as report:
            runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
            runner.run(testsuite)

if __name__ == '__main__':
    HTMLTestRunner.main()
    fp = file('my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='My unit test',
        description='This demonstrates the report output by HTMLTestRunner.'
    )




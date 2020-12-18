import unittest
import os
from lib.HTMLTestRunner_PY3 import HTMLTestRunner


class MyTest03(unittest.TestCase):
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'ExampleReport.html'
    # 实例化
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    #通过路径加载
    path = os.path.dirname(os.path.abspath(__file__))
    suite.addTest(loader.discover(path))
    #运行
    runner = unittest.TextTestRunner()
    runner.run(suite)




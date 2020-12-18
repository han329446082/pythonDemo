import allure
import pytest

@pytest.fixture(scope='session')
def login():
    print("用例先登陆")

@allure.step("步骤1：点击XXX")
def step1():
    print("step1")

@allure.step("步骤2：点击XXX")
def step2():
    print("step2")

@allure.feature('编辑页面')
class TestEditPage():

    @allure.story('这是一个XXX的用例1')
    def test_1(self,login):
        step1()
        step2()
        print('test_1')

    @allure.story('这是一个XXX的用例2')
    def test_2(self, login):
        step1()
        step2()
        print('test_2')

if __name__ == '__main__':
    # 注意生成测试报告 必须在命令行执行
    # pytest --alluredir ./reports testcases/pytest/test05.py
    # allure serve reports
    pytest.main(['--alluredir', './reports', 'test05.py'])







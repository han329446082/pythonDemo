import pytest
import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSearch(object):
    # 搜索框的XPATH
    keywords_input_x = "//div[@class='center-search clearfix']/form/input[@name='keywords']"
    #历史搜索词的XPATH
    history_words_x = "//div[@class='com-dropdown-wrapper']/div[@class='dropdown-search clearfix']/div[1]/ul/li[{index}]"
    # 热门搜索词的XPATH
    trending_words_x = "//div[@class='com-dropdown-wrapper']/div[@class='dropdown-search clearfix']/div[1]/ul/li[{index}]"


    #@allure.step('打开英文站首页，最大化111')
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.ybox.com/en')
        self.driver.maximize_window()

    #测试按照keywords进行搜索
    @allure.feature("搜索模块")
    @allure.story('搜索-关键字')
    @allure.title('测试用例名称：按照关键字进行搜索')
    def test_search_by_keywords(self):
        #输入关键字
        with allure.step('输入关键字'):
            self.driver.find_element(By.XPATH, self.keywords_input_x).send_keys('mask')
        #敲回车键
        with allure.step('敲回车'):
             self.driver.find_element(By.XPATH, self.keywords_input_x).send_keys(Keys.ENTER)
        #获取当前的URL
        curr_url = self.driver.current_url
        expected_url = 'https://www.ybox.com/en/search?track=search-input-0-mask&q=mask'
        assert curr_url == expected_url
        sleep(3)

    data = [1,2]
    @pytest.mark.parametrize('words_index',data)
    @allure.feature("搜索模块")
    @allure.story('搜索-热搜索词1')
    @allure.title('测试用例名称：按照热搜词的位置进行搜索')
    def test_search_by_trending(self,words_index):
        words_x2 = self.trending_words_x.format(index = words_index+1)
        # 光标定位到输入框，弹出搜索词弹层
        with allure.step('光标定位到输入框，弹出搜索词弹层'):
            self.driver.find_element(By.XPATH, self.keywords_input_x).click()
        sleep(3)
        #在搜索词弹层点击指定的搜索热词
        with allure.step('在搜索词弹层点击指定的搜索热词'):
            self.driver.find_element(By.XPATH, words_x2).click()
        #assert curr_url == expected_url
        sleep(3)

    #@allure.step('关闭浏览器1')
    def teardown_method(self):
        self.driver.quit()

if __name__ == '__main__':
    # 注意生成测试报告 必须在命令行执行
    # pytest --alluredir ./reports testcases/pytest/search.py
    # allure serve reports
    pytest.main(['--alluredir', './reports', 'search.py'])
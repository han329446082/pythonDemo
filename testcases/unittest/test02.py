import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MyTest02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.ybox.com/en')
        cls.driver.maximize_window()

    #测试按照keywords进行搜索
    def test_search_by_keywords(self):
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[2]/form/input[1]').send_keys('mask')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div[2]/form/input[1]').send_keys(Keys.ENTER)
        curr_url = self.driver.current_url
        expected_url = 'https://www.ybox.com/en/search?track=search-input-0-mask&q=mask'
        self.assertEqual(curr_url,expected_url)
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
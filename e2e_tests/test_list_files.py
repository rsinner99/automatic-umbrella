import logging
import sys
import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from trace_explorer.testsuite.base import Runner

logger = logging.getLogger("testrunners.selenium")
logger.setLevel(logging.DEBUG)


class ListFilesTestValid(Runner):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get("http://192.168.84.7/frontend/login")
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'password').send_keys('test1234test')
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, "button").click()
        return super().setUp()

    def tearDown(self) -> None:
        self.driver.get("http://192.168.84.7/frontend/")
        self.driver.find_element(By.LINK_TEXT, 'Logout')
        self.driver.close()
        return super().tearDown()

    def test(self):
        logger.debug('Run_script test 1...')
        
        # List files
        self.driver.get("http://192.168.84.7/frontend/")
        self.driver.find_element(By.LINK_TEXT, 'Files').click()
        self.driver.find_element(By.ID, "list_files_button").click()
        self.driver.find_element(By.XPATH, "//table/tbody/tr[last()]/td[1]/button").click()

        assert 'frontend/files/view' in self.driver.current_url
        

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("testrunners.selenium_base").setLevel(logging.DEBUG)
    unittest.main()

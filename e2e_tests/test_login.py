import os
import logging
import sys
import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from trace_explorer.testsuite.base import Runner
#from unittest import TestCase as Runner

logger = logging.getLogger("testrunners.selenium")
logger.setLevel(logging.DEBUG)

BASE_URL = os.environ.get("BASE_URL", "localhost")

class TestSelenium1(Runner):
    
    def test_neu(self):
        logger.debug('Test1...')
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(f"http://{BASE_URL}/frontend/")
        assert "Umbrella" in driver.title
        driver.close()

class TestSeleniumTest2(Runner):

    def test_2(self):
        logger.debug('Test2...')
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(f"http://{BASE_URL}/frontend/")
        assert "Umbrella" not in driver.title
        driver.close()

class TestSeleniumTest3(Runner):

    def test_3(self):
        logger.debug('Test3...')
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(f"http://{BASE_URL}/frontend/login")
        assert "Umbrella" in driver.title
        driver.find_element_by_name('username').send_keys('test')
        driver.find_element_by_name('password').send_keys('test1234test')
        time.sleep(1)
        driver.find_element_by_tag_name("button").click()
        driver.get(f"http://{BASE_URL}/frontend")
        driver.find_element_by_tag_name("button").click()
        driver.get(f"http://{BASE_URL}/frontend/logfqwf")
        assert "Umbrella" in driver.title
        driver.close()
        

class ScriptNotFoundTest(Runner):

    def test_4(self):
        logger.debug('ScriptNotFoundTest...')
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(f"http://{BASE_URL}/frontend/login")
        assert "Umbrella" in driver.title
        driver.find_element_by_name('username').send_keys('test')
        driver.find_element_by_name('password').send_keys('test1234test')
        time.sleep(1)
        driver.find_element_by_tag_name("button").click()
        driver.get(f"http://{BASE_URL}/frontend/tasks/")

        dropdown = Select(driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        driver.implicitly_wait(10)
        driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(34)
        driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys('1,2')
        driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        driver.find_element_by_xpath("//input[@value='Run task']").click()
        assert "Umbrella" in driver.title


class NewScriptNotFoundTest(Runner):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get(f"http://{BASE_URL}/frontend/login")
        self.driver.find_element_by_name('username').send_keys('test')
        self.driver.find_element_by_name('password').send_keys('test1234test')
        time.sleep(1)
        self.driver.find_element_by_tag_name("button").click()
        return super().setUp()

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

    def test_4(self):
        logger.debug('NewScriptNotFoundTest...')
        
        self.driver.get(f"http://{BASE_URL}/frontend/tasks/")

        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        self.driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(34)
        self.driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys('1,2')
        self.driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
        assert "Umbrella" not in self.driver.title

    def test_5(self):
        logger.debug('NewScriptNotFoundTest...')
        
        self.driver.get(f"http://{BASE_URL}/frontend/tasks/")

        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        self.driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(3)
        self.driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys('1,2,3')
        self.driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
        assert "Umbrella" not in self.driver.title

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("testrunners.selenium_base").setLevel(logging.DEBUG)
    unittest.main()

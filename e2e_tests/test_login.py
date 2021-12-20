import logging
import sys
import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#from testrunners.base import Runner
from unittest import TestCase as Runner

logger = logging.getLogger("testrunners.selenium")
logger.setLevel(logging.DEBUG)

class TestSelenium1(Runner):
    
    def test_neu(self):
        logger.debug('Test1...')
        s=Service(ChromeDriverManager().install())
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(service=s, options=options)
        driver.get("http://192.168.84.7/frontend/")
        assert "Umbrella" in driver.title
        driver.close()

class TestSeleniumTest2(Runner):

    def test_2(self):
        logger.debug('Test2...')
        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.get("http://192.168.84.7/frontend/")
        assert "Umbrella" not in driver.title
        driver.close()

class TestSeleniumTest3(Runner):

    def test_3(self):
        logger.debug('Test3...')
        options = webdriver.ChromeOptions()
        #options.add_experimental_option("detach", True)
        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, chrome_options=options)
        driver.get("http://192.168.84.7/frontend/login")
        assert "Umbrella" in driver.title
        driver.find_element_by_name('username').send_keys('test')
        driver.find_element_by_name('password').send_keys('test1234test')
        time.sleep(1)
        driver.find_element_by_tag_name("button").click()
        driver.get("http://192.168.84.7/frontend")
        driver.find_element_by_tag_name("button").click()
        driver.get("http://192.168.84.7/frontend/logfqwf")
        assert "Umbrella" in driver.title
        driver.close()
        

class ScriptNotFoundTest(Runner):

    def test_4(self):
        logger.debug('ScriptNotFoundTest...')
        options = webdriver.ChromeOptions()
        #options.add_experimental_option("detach", True)
        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, chrome_options=options)
        driver.get("http://192.168.84.7/frontend/login")
        assert "Umbrella" in driver.title
        driver.find_element_by_name('username').send_keys('test')
        driver.find_element_by_name('password').send_keys('test1234test')
        time.sleep(1)
        driver.find_element_by_tag_name("button").click()
        driver.get("http://192.168.84.7/frontend/tasks/")

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
        s=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("http://192.168.84.7/frontend/login")
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
        
        self.driver.get("http://192.168.84.7/frontend/tasks/")

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
        
        self.driver.get("http://192.168.84.7/frontend/tasks/")

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

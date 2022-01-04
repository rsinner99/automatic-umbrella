import logging
import sys
import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from tracing_rca.testsuite.base import Runner

logger = logging.getLogger("testrunners.selenium")
logger.setLevel(logging.DEBUG)

class BaseTest(Runner):
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

class Test019(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 019...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        self.driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys(1)
        self.driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test020(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 020...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        self.driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(9)
        self.driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys(1)
        self.driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test021(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 021...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        self.driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys("2")
        self.driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test022(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 021...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        self.driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys("1")
        self.driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test023(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 023...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        self.driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys("1")
        self.driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title

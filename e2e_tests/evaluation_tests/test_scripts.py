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

class Test001(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 001...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('scripts.run_script')
        self.driver.find_element_by_id('run_script_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_id_peers').send_keys('1')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test002(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 002...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('scripts.run_script')
        self.driver.find_element_by_id('run_script_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_id_peers').send_keys('2')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test003(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 003...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('scripts.run_script')
        self.driver.find_element_by_id('run_script_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_id_peers').send_keys('1')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test004(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 004...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('scripts.run_script')
        self.driver.find_element_by_id('run_script_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_id_peers').send_keys('3')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test005(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 005...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('scripts.run_script')
        self.driver.find_element_by_id('run_script_id_doc').send_keys(23)
        self.driver.find_element_by_id('run_script_id_peers').send_keys('1')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test006(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 006...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('scripts.run_script')
        self.driver.find_element_by_id('run_script_id_doc').send_keys(-1)
        self.driver.find_element_by_id('run_script_id_peers').send_keys('1')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test007(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 007...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('scripts.run_script')
        self.driver.find_element_by_id('run_script_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_id_peers').send_keys('-1')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title
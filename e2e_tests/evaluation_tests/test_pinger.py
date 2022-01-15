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


class Test010(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 010...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('pinger.ping_host')
        self.driver.find_element_by_id('ping_host_id_host').send_keys("172.17.0.1")
        self.driver.find_element_by_id('ping_host_id_timeout').send_keys(2)

        time.sleep(2)
        result = self.driver.find_element(By.ID, 'id_result').text

        assert "echo-reply" in result


class Test011(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 011...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('pinger.ping_host')
        self.driver.find_element_by_id('ping_host_id_host').send_keys("172.17.0.1")
        self.driver.find_element_by_id('ping_host_id_timeout').send_keys(0.0001)

        time.sleep(2)
        result = self.driver.find_element(By.ID, 'id_result').text

        assert "not reachable" in result


class Test012(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 012...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('pinger.ping_host')
        self.driver.find_element_by_id('ping_host_id_host').send_keys("172.17.0.15")
        self.driver.find_element_by_id('ping_host_id_timeout').send_keys(2)

        time.sleep(2)
        result = self.driver.find_element(By.ID, 'id_result').text

        assert "not reachable" in result


class Test013(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 013...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('pinger.ping_host')
        self.driver.find_element_by_id('ping_host_id_host').send_keys("172.17.0.15.1")
        self.driver.find_element_by_id('ping_host_id_timeout').send_keys(2)

        time.sleep(2)
        result = self.driver.find_element(By.ID, 'id_result').text

        assert "not reachable" in result



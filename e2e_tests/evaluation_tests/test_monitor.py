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


class Test008(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 008...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Home').click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/button").click()
        time.sleep(10)

        assert "Umbrella" in self.driver.title


class Test009(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 009...')

        self.driver.get("http://192.168.84.7/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Home').click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/button").click()
        time.sleep(10)

        assert "Umbrella" in self.driver.title
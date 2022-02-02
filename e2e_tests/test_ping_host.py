import os
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

BASE_URL = os.environ.get("BASE_URL", "localhost")

class PingHostTestValid(Runner):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get(f"http://{BASE_URL}/frontend/login")
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'password').send_keys('test1234test')
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, "button").click()
        return super().setUp()

    def tearDown(self) -> None:
        self.driver.get(f"http://{BASE_URL}/frontend/")
        self.driver.find_element(By.LINK_TEXT, 'Logout')
        self.driver.close()
        return super().tearDown()

    def test(self):
        logger.debug('Run_script test 1...')

        self.driver.get(f"http://{BASE_URL}/frontend/")
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        task_choice = Select(self.driver.find_element(By.ID, "id_taskname"))
        task_choice.select_by_value("pinger.ping_host")

        self.driver.find_element(By.ID, "ping_host_id_host").send_keys('172.17.0.0/30')
        self.driver.find_element(By.ID, "ping_host_id_timeout").send_keys('1')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
        output = self.driver.find_element(By.NAME, "result").text
        assert "172.17.0.1" in output
        

class PingHostTestInvalid(Runner):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get(f"http://{BASE_URL}/frontend/login")
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'password').send_keys('test1234test')
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, "button").click()
        return super().setUp()

    def tearDown(self) -> None:
        self.driver.get(f"http://{BASE_URL}/frontend/")
        self.driver.find_element(By.LINK_TEXT, 'Logout')
        self.driver.close()
        return super().tearDown()

    def test(self):
        logger.debug('Run_script test 1...')

        self.driver.get(f"http://{BASE_URL}/frontend/")
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        task_choice = Select(self.driver.find_element(By.ID, "id_taskname"))
        task_choice.select_by_value("pinger.ping_host")

        self.driver.find_element(By.ID, "ping_host_id_host").send_keys('172.17.1...3')
        self.driver.find_element(By.ID, "ping_host_id_timeout").send_keys('1')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
        output = self.driver.find_element(By.NAME, "result").text
        assert "172.17.0.1" in output


class PingHostTestInvalid2(Runner):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get(f"http://{BASE_URL}/frontend/login")
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'password').send_keys('test1234test')
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, "button").click()
        return super().setUp()

    def tearDown(self) -> None:
        self.driver.get(f"http://{BASE_URL}/frontend/")
        self.driver.find_element(By.LINK_TEXT, 'Logout')
        self.driver.close()
        return super().tearDown()

    def test(self):
        logger.debug('Run_script test 1...')

        self.driver.get(f"http://{BASE_URL}/frontend/")
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        task_choice = Select(self.driver.find_element(By.ID, "id_taskname"))
        task_choice.select_by_value("pinger.ping_host")

        self.driver.find_element(By.ID, "ping_host_id_host").send_keys('172.17.0.1')
        self.driver.find_element(By.ID, "ping_host_id_timeout").send_keys('SHOULD BE A NUMBER')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
        output = self.driver.find_element(By.NAME, "result").text
        assert "172.17.0.1" in output

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("testrunners.selenium_base").setLevel(logging.DEBUG)
    unittest.main()

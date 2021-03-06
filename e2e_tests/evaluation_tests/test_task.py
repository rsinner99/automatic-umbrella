import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from trace_explorer.testsuite.base import Runner

logger = logging.getLogger("testrunners.selenium")
logger.setLevel(logging.DEBUG)

BASE_URL = os.environ.get("BASE_URL", "localhost")

class BaseTest(Runner):
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


class Test014(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 014...')

        self.driver.get(f"http://{BASE_URL}/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('scripts.run_script')
        self.driver.find_element_by_id('run_script_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_id_peers').send_keys('-1')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test015(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 015...')

        self.driver.get(f"http://{BASE_URL}/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        self.driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(1)
        self.driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys(1)
        self.driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test016(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 016...')

        self.driver.get(f"http://{BASE_URL}/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('calc.estimate_pi')
        self.driver.find_element_by_id('estimate_pi_id_interval').send_keys(1000000)

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title



class Test017(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 017...')

        self.driver.get(f"http://{BASE_URL}/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('calc.estimate_pi')
        self.driver.find_element_by_id('estimate_pi_id_interval').send_keys(100000000)

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title


class Test018(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 018...')

        self.driver.get(f"http://{BASE_URL}/frontend/")
        
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('calc.estimate_pi')
        self.driver.find_element_by_id('estimate_pi_id_interval').send_keys(10)

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title

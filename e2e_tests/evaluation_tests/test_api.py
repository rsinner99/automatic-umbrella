import logging
import requests
import time
import json

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from trace_explorer.testsuite.base import Runner

logger = logging.getLogger("testrunners.selenium")
logger.setLevel(logging.DEBUG)

BASE_URL = "http://192.168.84.7/"

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


class Test024(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 024...')

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


class Test025(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 025...')

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


class Test026(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 026...')

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


class Test027(BaseTest):
    def test(self):
        logger.debug('Evaluation Test 027...')

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


def get_token(username, password):
    data = {
        'username': username,
        'password': password
    }
    resp = requests.post(BASE_URL + "api/token/", data=data)
    if resp.status_code == 200:
        return resp.json()['access']
    else:
        raise Exception('Token generation failed')


class Test028(Runner):
    def setUp(self):
        token = get_token('test', 'test1234test')
        self.header = {
            'Authorization': 'Bearer ' + token
        }

    def test_task(self):
        data = {
            "taskname": "task.invalid_name",
            "name": "TestPostman"
        }
        resp = requests.post(BASE_URL + "api/task/generic_run", data=json.dumps(data), headers=self.header)
        assert resp.status_code == 200

        task_id = resp.json()['task_id']
        params = {
            'task': task_id
        }
        resp = requests.get(BASE_URL + "api/task/result", params=params, headers=self.header)
        counter = 0
        while resp.json()['status'] == 'PENDING' and counter < 10:
            time.sleep(1)
            resp = requests.get(BASE_URL + "api/task/result", params=params, headers=self.header)
            counter += 1

        assert resp.json()['status'] == 'SUCCESS'


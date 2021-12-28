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


class RunScriptTestValid(Runner):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get("http://192.168.84.7/frontend/login")
        self.driver.find_element_by_name('username').send_keys('test')
        self.driver.find_element_by_name('password').send_keys('test1234test')
        time.sleep(1)
        self.driver.find_element_by_tag_name("button").click()
        return super().setUp()

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

    def test(self):
        logger.debug('Run_script test 1...')
        
        # Creating a peer
        self.driver.get("http://192.168.84.7/frontend/")
        self.driver.find_element(By.LINK_TEXT, 'Peers').click()
        self.driver.find_element(By.LINK_TEXT, 'Add peer').click()
        ip_address_field = self.driver.find_element(By.ID, 'id_ip_address')
        port_field = self.driver.find_element(By.ID, 'id_ssh_port')
        hostname_field = self.driver.find_element(By.ID, 'id_hostname')
        username_field = self.driver.find_element(By.ID, 'id_username')
        password_field = self.driver.find_element(By.ID, 'id_password')
        pk_field = self.driver.find_element(By.ID, 'id_private_key')
        passphrase_field = self.driver.find_element(By.ID, 'id_passphrase')
        os_field = Select(self.driver.find_element(By.ID, 'id_os'))

        ip_address_field.send_keys('172.17.0.1')
        port_field.send_keys(22)
        hostname_field.send_keys('docker host')
        username_field.send_keys('rsinner')
        password_field.send_keys('invalid')
        pk_field.send_keys('')
        passphrase_field.send_keys('')
        os_field.select_by_value('windows')

        self.driver.find_element_by_xpath("//input[@value='Save']").click()

        self.driver.find_element(By.LINK_TEXT, 'Peers').click()
        lastRow = self.driver.findElement(By.xpath("(//table[1]/tbody/tr)[last()]"))
        peer_id = lastRow.findlement(By.xpath("(//td[1]")).text

        # Creating a doc
        self.driver.find_element(By.LINK_TEXT, 'Docs').click()
        self.driver.find_element(By.LINK_TEXT, 'Add doc').click()
        name_field = self.driver.find_element(By.ID, 'id_name')
        content_field = self.driver.find_element(By.ID, 'id_content')
        type_field = Select(self.driver.find_element(By.ID, 'id_type'))
        os_field = Select(self.driver.find_element(By.ID, 'id_os'))

        name_field.send_keys('New Test Doc')
        content_field.send_keys('ls -la')
        type_field.select_by_value('sh')
        os_field.select_by_value('windows')

        self.driver.find_element_by_xpath("//input[@value='Save']").click()

        self.driver.find_element(By.LINK_TEXT, 'Docs').click()
        lastRow = self.driver.findElement(By.xpath("(//table[1]/tbody/tr)[last()]"))
        doc_id = lastRow.findlement(By.xpath("(//td[1]")).text

        # Creating a task
        self.driver.find_element(By.LINK_TEXT, 'Tasks').click()
        dropdown = Select(self.driver.find_element_by_id('id_taskname'))
        dropdown.select_by_value('hello.run_script_output_to_storage')
        self.driver.find_element_by_id('run_script_output_to_storage_id_doc').send_keys(doc_id)
        self.driver.find_element_by_id('run_script_output_to_storage_id_peers').send_keys(peer_id)
        self.driver.find_element_by_id('run_script_output_to_storage_id_filename').send_keys('test.txt')

        self.driver.find_element_by_xpath("//input[@value='Run task']").click()
        time.sleep(10)
       
        assert "Umbrella" in self.driver.title
        

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("testrunners.selenium_base").setLevel(logging.DEBUG)
    unittest.main()

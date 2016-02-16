#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""firestorm selenium tests

testing different unittests for firestorm website
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class FirestormTests(unittest.TestCase):
    """test cases for firstorm website"""

    def setUp(self):
        """creates a webdriver"""
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)

    # def test_login_firestorm(self):
    #     """tests login page and validates successful login"""
    #     driver = self.driver
    #     driver.get('http://localhost:8000')
    #     self.assertIn('Log in', driver.title)
    #     email = driver.find_element_by_name('email')
    #     email.send_keys('neqel')
    #     email.send_keys(Keys.RETURN)
    #     self.assertIn('User Page', driver.title)

    def test_user_page_form(self):
        """tests adding a new item with the form"""
        driver = self.driver
        driver.get('http://localhost:8000')
        email = driver.find_element_by_name('email')
        email.send_keys('neqel')
        email.send_keys(Keys.RETURN)
        driver = self.driver
        assert 'Add a topic!' in driver.page_source

        # Enter Subject
        subject = driver.find_element_by_name('subject')
        subject.send_keys('selenium')
        # Enter Url
        url = driver.find_element_by_name('url')
        url.send_keys('http://selenium-python.readthedocs.org/index.html')
        # Enter Description
        desc = driver.find_element_by_name('description')
        desc.send_keys('Teach us more then Brett Could')
        # Set depth
        depth = Select(driver.find_element_by_name('depth'))
        depth.select_by_value('B')
        depth.select_by_value('E')
        # click submit
        driver.find_element_by_xpath('//input[2]').click()


    def tearDown(self):
        """closes webdriver"""
        self.driver.close()

# main call
if __name__ == "__main__":
    unittest.main()

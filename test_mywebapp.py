#!/usr/local/bin/python

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class MyWebAppTestCase(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        self.browser = webdriver.Chrome(options=options)

    def testClickButtonOK(self):
        browser = self.browser
        browser.get("file:////home/circleci/mywebapp-repo/index.html")
        button = browser.find_element_by_tag_name('button')
        time.sleep(1)
        button.click()
        element = browser.find_element_by_tag_name('p')
        self.assertIn("Hello World!", element.text)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

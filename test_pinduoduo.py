# -*- coding: utf-8 -*-
# __author__=luhu
import unittest
import os
import time
from macaca import WebDriver
from macaca import Keys
from retrying import retry

desired_caps = {
    'platformName': 'android',
    'app': 'C:/pinduoduo_gw_pc_latest.apk'

    }
server_url = {
    'hostname': 'localhost',
    'port': 3456
}


def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver


def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver


class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.initDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    @retry
    def initDriver(cls):
        print("Retry connecting server...")
        cls.driver.init()

    def test_01_login(self):
        self.driver.wait_for_element('class_name', 'android.view.View').click()
        time.sleep(3)
        self.driver.wait_for_elements('class_name', 'android.widget.RelativeLayout')[5].click()
        time.sleep(3)
        self.driver.touch('press', {
            'x': 279,
            'y': 300,
        })
        time.sleep(3)
        self.driver.touch('press', {
            'x': 200,
            'y': 600,
        })
        time.sleep(3)
        # self.driver.element('class_name', 'android.widget.TextView').click()
        # time.sleep(1)
        # self.driver.element('class_name', 'android.widget.TextView').click()
        # time.sleep(1)
        # self.driver.elements('class_name', 'android.widget.Button')[0].click()
        # self.driver.back()
        # self.driver.keys(Keys.ENTER.value + Keys.ESCAPE.value)


if __name__ == '__main__':
    unittest.main()
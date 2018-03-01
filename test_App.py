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
    # 'app': 'C:/android_app_bootstrap-debug.apk'
    # 'app': 'C:/google.apk'

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
        el = self.driver.elements('class_name', 'android.widget.EditText')[0].send_keys('中文+Test+12345678')
        el = self.driver.elements('class_name', 'android.widget.EditText')[1].send_keys('111111')
        time.sleep(1)
        # self.driver.keys(Keys.ENTER.value + Keys.ESCAPE.value)
        self.driver.element_by_name('Login').click()

    def test_02_scroll_tableview(self):
        self.driver.wait_for_element('name', 'HOME').click()
        self.driver.wait_for_element('name', 'list').click()
        self.driver.back()

    def test_03_gesture(self):
        self.driver.wait_for_element('name', 'HOME').click()
        self.driver.wait_for_element('name', 'list').click()
        time.sleep(3)
        self.driver.wait_for_element('name', 'Alert').click()
        time.sleep(3)
        self.driver .accept_alert()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.wait_for_element('name', 'Gesture').click()
        time.sleep(3)
        self.driver .touch('tap', {
              'x': 100,
              'y': 100
            })
        time.sleep(5)
        self.driver .touch('doubleTap', {
              'x': 100,
              'y': 100
            })
        time.sleep(3)
        self.driver.touch('press', {
              'x': 100,
              'y': 100,
              'steps': 100
            })
        time.sleep(3)
        self.driver.touch('drag', {
              'fromX': 100,
              'fromY': 100,
              'toX': 100,
              'toY': 600,
              'steps': 100
            })
        time.sleep(5)
        self.driver.back()
        self.driver.back()

    def test_04_webview(self):
        self.driver.wait_for_element('name', 'Webview').click()
        time.sleep(5)
        self.driver.save_screenshot('./webView.png')     # save screen shot
        self.driver.wait_for_element('name', 'pushView').click()
        self.driver.wait_for_element('name', 'popView').click()

    def test_05_web(self):
        self.driver.wait_for_element('name', 'Baidu').click()
        time.sleep(5)
        self.driver.save_screenshot("./baidu.png")
        self.driver.wait_for_element('id', 'index-kw') .send_keys('macaca')
        self.driver.wait_for_element('id', 'index-bn').click()

    def test_06_logout(self):
        switch_to_native(self.driver).wait_for_element_by_name('PERSONAL').click()
        self.driver.wait_for_element('name', 'Logout').click()


if __name__ == '__main__':
    unittest.main()
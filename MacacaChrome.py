# -*- coding: utf-8 -*-
# __author__=luhu
import unittest
from macaca import WebDriver
from time import sleep

from retrying import retry

desired_caps = {
    'platformName': 'Android',  # // iOS, Android, Desktop
    'browserName': 'Chrome',    # // Chrome, Electron
    # 'app': 'C:/google.apk'       # Only for mobile
}

# 对应Macaca服务的ip和端口号。
server_url = {
    'hostname': 'localhost',
    'port': 3456
}


def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
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

    def test_search_macaca(self):
        self.driver.get('https://www.baidu.com')
        switch_to_webview(self.driver).wait_for_element.element('id', "index-kw").send_keys("macaca")
        self.driver.element('id', "su").click()
        sleep(2)
        title = self.driver.title
        self.assertTrue('macaca', title)


if __name__ == '__main__':
    unittest.main()
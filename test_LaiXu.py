# -*- coding: utf-8 -*-
# __author__=luhu
import unittest
from macaca import WebDriver
from time import sleep

from retrying import retry

desired_caps = {
    'platformName': 'Desktop',  # // iOS, Android, Desktop
    'browserName': 'Chrome',    # // Chrome, Electron
    # 'app': 'C:/google.apk'       # Only for mobile
}

# 对应Macaca服务的ip和端口号。
server_url = {
    'hostname': 'localhost',
    'port': 3456
}


class LaiXuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.initDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @classmethod
    @retry
    def initDriver(cls):
        print("Retry connecting server...")
        cls.driver.init()

    def test_search_LaiXu(self):
        self.driver.get('http://192.168.1.102:7777')


if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
# __author__=luhu
from macaca import WebDriver
import time

desired_caps = {
    'browserName': 'Chrome',  # Electon, Safari(iOS).
    'platformName': 'Desktop',  # iOS, Android, Desktop
    # 'platformVersion': '*',
    'autoAcceptAlerts': True
}

server_url = 'https://www.baidu.com'
driver = WebDriver(desired_caps)
driver.init()
driver.maximize_window()
driver.get(server_url)
driver.element_by_id("kw")
driver.send_keys("macaca")
driver.element_by_id("su").click()
print(driver.title)
driver.wait_for_element('id', 'head')
driver.close()
# -*- coding: utf-8 -*-
# __author__=luhu
from macaca import WebDriver
import time

desired_caps = {
    'browserName': 'Chrome',  # Electon, Safari(iOS).Chrome
    'platformName': 'Desktop',  # iOS, Android, Desktop
    # 'platformVersion': '*',
    'autoAcceptAlerts': True
}

server_url = 'https://www.baidu.com'
driver = WebDriver(desired_caps)
driver.init()
driver.maximize_window()
driver.get(server_url)
driver.element('id', "kw")
driver.send_keys("macaca")
driver.element('id', "su").click()
print(driver.title)
time.sleep(4)
driver.close()

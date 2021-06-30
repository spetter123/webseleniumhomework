from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestDeBug:

    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        print("打开主页")

    def test_debug(self):
        group_list = []
        # self.driver.find_element(By.XPATH, '//*[@id="1688850214948671_anchor"]/span').click()
        # self.driver.find_element(By.XPATH, '/html/body/ul/li[1]/a').click()
        # self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input'). \
        #     send_keys("testgroup")
        # self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        # sleep(3)
        print(group_list)
        result = self.driver.find_element(By.XPATH, '//*[@id="1688850214948671"]/ul').get_attribute("textContent")
        print(result)
        group_list.append("".join(result.split()))
        print(group_list)


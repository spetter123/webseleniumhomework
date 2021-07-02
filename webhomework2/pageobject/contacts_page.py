from time import sleep
from selenium.webdriver.common.by import By
from webhomework2.pageobject.basepage import BasePage


class ContactsPage(BasePage):
    _FIRSTPOINT = (By.XPATH, '//*[@id="1688850214948671_anchor"]/span')
    _ADD_GROUP = (By.XPATH, '/html/body/ul/li[1]/a')
    _ADD_GROUP_NAME = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input')
    _GROUP_NAME = "testgroup"
    _ALLOW = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')
    _GROUP_LIST = (By.XPATH, '//*[@id="1688850214948671"]/ul')

    def add_group(self):
        group_list = []
        # self.driver.find_element(By.XPATH, '//*[@id="1688850214948671_anchor"]/span').click()
        # self.driver.find_element(By.XPATH, '/html/body/ul/li[1]/a').click()
        # self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').\
        #     send_keys("testgroup")
        # self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        # sleep(3)
        # result = self.driver.find_element(By.XPATH, '//*[@id="1688850214948671"]/ul').get_attribute("textContent")

        self.find_click(*self._FIRSTPOINT)
        self.find_click(*self._ADD_GROUP)
        self.find_send(*self._ADD_GROUP_NAME, self._GROUP_NAME)
        self.find_click(*self._ALLOW)
        sleep(3)
        result = self.find_get(*self._GROUP_LIST, "textContent")

        # 直接使用group_list.append(result)返回的文本中会加入“\xa0”不间断空白符，可以使用"".join(result.split())替换掉result解决，
        group_list.append("".join(result.split()))
        return group_list

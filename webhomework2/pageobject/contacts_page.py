from time import sleep

from selenium.webdriver.common.by import By

from webhomework2.pageobject.basepage import BasePage


class ContactsPage(BasePage):
    def add_group(self):
        group_list = []
        self.driver.find_element(By.XPATH, '//*[@id="1688850214948671_anchor"]/span').click()
        self.driver.find_element(By.XPATH, '/html/body/ul/li[1]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').\
            send_keys("testgroup")
        self.driver.find_element(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        sleep(3)
        result = self.driver.find_element(By.XPATH, '//*[@id="1688850214948671"]/ul').get_attribute("textContent")
        # \xa0:是不间断空白符 & nbsp;此处group_list.append(result)会加入不间断空白符，可以使用"".join(result.split())替换掉result解决
        # 此处原理未知
        # group_list.append(result)
        group_list.append("".join(result.split()))
        return group_list

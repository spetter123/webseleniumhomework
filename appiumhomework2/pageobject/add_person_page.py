from telnetlib import EC

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from appiumhomework2.pageobject.base_page import BasePage
from appiumhomework2.pageobject.edit_person_page import EditPersonPage


class AddPersonPage(BasePage):
    _MANUAL_ELEMENT = (MobileBy.XPATH, "//*[@text = '手动输入添加']")
    _TOAST_ELEMENT = (MobileBy.XPATH, "//*[@class='android.widget.Toast']", 'text')

    def goto_edit_page(self):
        self.find_click(*self._MANUAL_ELEMENT)
        return EditPersonPage(self.driver)

    def get_result(self):
        result = self.find_get_attribute(*self._TOAST_ELEMENT)
        # result = self.find_get_attribute(MobileBy.XPATH, "//*[@class='android.widget.Toast']", 'text')
        # result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return result

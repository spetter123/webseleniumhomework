from appium.webdriver.common.mobileby import MobileBy
from appiumhomework2.pageobject.base_page import BasePage
from appiumhomework2.pageobject.contact_page import ContactPage


class MainPage(BasePage):
    _CONTACT_ELEMENT = (MobileBy.XPATH, "//*[@text = '通讯录']")

    def goto_contact_page(self):
        self.find_click(*self._CONTACT_ELEMENT)
        return ContactPage(self.driver)

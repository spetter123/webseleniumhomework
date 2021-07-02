from selenium.webdriver.common.by import By

from webhomework2.pageobject.basepage import BasePage
from webhomework2.pageobject.contacts_page import ContactsPage


class MainPage(BasePage):
    _CONTACTS = (By.ID, "menu_contacts")

    def goto_contact(self):
        # self.driver.find_element(*self._CONTACTS).click()
        self.find_click(*self._CONTACTS)
        # 此处漏传self.driver的话进入，contactoage后再次初始化时driver是None因此会重新初始化一次
        return ContactsPage(self.driver)

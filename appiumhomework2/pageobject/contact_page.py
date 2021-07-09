from appium.webdriver.common.mobileby import MobileBy
from appiumhomework2.pageobject.add_person_page import AddPersonPage
from appiumhomework2.pageobject.base_page import BasePage


class ContactPage(BasePage):
    _ADD_PERSON_ELEMENT = (MobileBy.XPATH, '//*[@text = "添加成员"]')
    _MANAGE_ELEMENT = (MobileBy.ID, "com.tencent.wework:id/hcd")

    def goto_add_page(self):
        self.find_click(*self._ADD_PERSON_ELEMENT)
        return AddPersonPage(self.driver)

    def goto_manage_page(self):
        self.find_click(*self._MANAGE_ELEMENT)
        from appiumhomework2.pageobject.manage_page import ManagePage
        return ManagePage(self.driver)

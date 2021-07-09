from appium.webdriver.common.mobileby import MobileBy

from appiumhomework2.pageobject.base_page import BasePage


class SetPersonPage(BasePage):
    _DEL_ELEMENT = (MobileBy.XPATH, "//*[@text='删除成员']")
    _CONFIRM_ELEMENT = (MobileBy.XPATH, "//*[@text='确定']")

    def del_person(self):
        self.find_click(*self._DEL_ELEMENT)
        self.find_click(*self._CONFIRM_ELEMENT)
        from appiumhomework2.pageobject.manage_page import ManagePage
        return ManagePage(self.driver)

from appium.webdriver.common.mobileby import MobileBy

from appiumhomework2.pageobject.base_page import BasePage


class EditPersonPage(BasePage):
    _NAME_ELEMENT = (MobileBy.XPATH, '//*[@text = "必填" and @index = 2]')
    _MEMBER_ELEMENT = (MobileBy.XPATH, '//*[@text = "必填" and @index = 0]')
    _SAVE_ELEMENT = (MobileBy.XPATH, '//*[@text = "保存"]')

    def add_person(self, nickname, member):
        self.find_send_keys(*self._NAME_ELEMENT, nickname)
        self.find_send_keys(*self._MEMBER_ELEMENT, member)
        self.find_click(*self._SAVE_ELEMENT)
        from appiumhomework2.pageobject.add_person_page import AddPersonPage
        return AddPersonPage(self.driver)

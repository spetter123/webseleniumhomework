from appium.webdriver.common.mobileby import MobileBy

from appiumhomework2.pageobject.base_page import BasePage
from appiumhomework2.pageobject.set_person_page import SetPersonPage


class ManagePage(BasePage):
    _PERSON_LIST = (MobileBy.XPATH, "//*[@class = 'android.widget.ListView']", 'text')

    def goto_set_person_page(self, nickname):
        # self.find_click(MobileBy.XPATH, f"//*[@text = '{nickname}']")
        self.swipe_find(MobileBy.XPATH, nickname).click()
        return SetPersonPage(self.driver)

    def find_person(self):
        result = self.find_get_attribute(*self._PERSON_LIST)
        return result

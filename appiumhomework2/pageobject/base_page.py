from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, element, locator):
        logging.info(f'find:element={element};locator={locator}')
        return self.driver.find_element(element, locator)

    def find_click(self, element, locator):
        logging.info(f'find_click:element={element};locator={locator}')
        return self.find(element, locator).click()

    def find_send_keys(self, element, locator, message):
        logging.info(f'find_send_keys:element={element};locator={locator}')
        return self.find(element, locator).send_keys(message)

    def find_get_attribute(self, element, locator, attribute_type):
        logging.info(f'find_get_attribute:element={element};locator={locator};attribute_type={attribute_type}')
        result = self.driver.find_element(element, locator).get_attribute(attribute_type)
        return result

    def swipe_find(self, element, text, num=3):
        logging.info(f'swipe_find:text = {text}')
        # 重置隐式等待
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                logging.info(f"element={element}, text={text}")
                element = self.driver.find_element(element, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000

                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
                logging.info(f"start_pos:({start_x}, {start_y})====> end_pos:({end_x}, {end_y})")

            if i == num - 1:
                # 还原隐式等待
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了 {i} 次，未找到")

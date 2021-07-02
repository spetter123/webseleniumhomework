import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _WX_ADDRESS = "https://work.weixin.qq.com/wework_admin/frame#index"

    def __init__(self, driver_base: WebDriver = None):
        if driver_base is None:
            # 复用浏览器
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(3)
            self.driver.get(self._WX_ADDRESS)
            # # 使用cookie登录
            # self.driver = webdriver.Chrome()
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # with open("cookies.yaml", encoding="UTF-8") as f:
            #     cookies = yaml.safe_load(f)
            # for cookie in cookies:
            #     self.driver.add_cookie(cookie)
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            print("打开主页")
        else:
            self.driver = driver_base

    def find_click(self, element, locator):
        return self.driver.find_element(element, locator).click()

    def find_send(self, element, locator, text):
        return self.driver.find_element(element, locator).send_keys(text)

    def find_get(self, element, locator, gettype):
        return self.driver.find_element(element, locator).get_attribute(gettype)



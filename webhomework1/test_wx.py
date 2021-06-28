# 通过Cookie或者Remote浏览器复用完成添加联系人测试用例
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAdd:
    def setup(self):
        # 复用浏览器
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 获取cookies
        cookies = self.driver.get_cookies()
        with open("./cookies.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookies, f)
        self.driver.implicitly_wait(3)

    # def teardown(self):
    #     # self.driver.quit()
    #     print("测试结束")

    def test_get_cookies(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//*[@data-name='contacts']/div/div[2]/div/div[2]/div[3]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("张三")
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys("zhangsan")
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys("18653785695")
        self.driver.find_element(By.XPATH, "//*[@data-name='contacts']/div/div[2]/div/div[4]/div/form/div[3]/a[2]").click()
        sleep(2)
        name = self.driver.find_element(By.XPATH, '//*[@id="member_list"]').get_attribute("textContent")
        assert "张三" in name



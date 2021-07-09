# 实现添加联系人功能的 PO 封装
# BasePage 的封装
# 初始化方法
# find 方法
# find_and_click 方法
# handle_exception 方法
# 使用标准 log 取代 print
# logging.baseConfig(level=logging.DEBUG)
# 在具体的 action 中加入 log 方便追踪
# 完成参数化
# 完成allure报告
import pytest
import allure
from appiumhomework2.pageobject.app import App
from appiumhomework2.pageobject.main_page import MainPage


class TestAddPerson:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start_app().goto_main_page()
        pass

    def teardown(self):
        pass

    def teardown_class(self):
        self.app.quit_app()

    @allure.story("增加联系人")
    @pytest.mark.parametrize("nickname, member", [("王五", 15285589658)], ids=["wangwu+15285589658"])
    def test_add_person(self, nickname, member):
        result = self.main.goto_contact_page().goto_add_page().goto_edit_page().add_person(nickname, member).get_result()
        assert "添加成功" == result

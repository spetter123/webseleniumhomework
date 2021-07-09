# 实现删除联系人功能的 PO 封装
import pytest
import allure
from appiumhomework2.pageobject.app import App
from appiumhomework2.pageobject.main_page import MainPage


class TestDelPerson:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start_app().goto_main_page()

    def teardown(self):
        pass

    def teardown_class(self):
        # self.app.quit_app()
        pass

    @allure.story("删除联系人")
    @pytest.mark.parametrize("nickname", ["王五"], ids=["wangwu"])
    def test_del_person(self, nickname):
        result = self.main.goto_contact_page().goto_manage_page().goto_set_person_page(nickname).del_person().find_person()
        assert nickname not in result

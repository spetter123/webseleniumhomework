# 使用po思想完成添加部门操作的自动化测试

from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from webhomework2.pageobject.main_page import MainPage


class TestAddGroup:
    def setup(self):
        self.main = MainPage()

    def test_add_group(self):
        group_list = self.main.goto_contact().add_group()
        assert "testgroup" in group_list


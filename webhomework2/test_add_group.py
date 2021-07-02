# 使用po思想完成添加部门操作的自动化测试
# basepage封装-clear
# 添加失败用例检测-clear
# 提取页面元素-clear
# 封装样板代码-clear
# 添加起始页的url-clear
# https://gitlab.stuq.ceshiren.com/ck/ck19/hogwartssdet19/-/blob/master/test_selenium/po/main_page.py

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


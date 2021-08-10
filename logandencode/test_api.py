import logging

import pytest

from logandencode.conftest import logger


class TestApi:
    @pytest.mark.parametrize(['a', 'b'], [["张三", "李四"]])
    def test_api1(self, a, b):
        logger.info("test start")
        print(f"我们是{a}和{b}")
        logger.info("test over")

    @pytest.mark.parametrize('a', ["张三", "李四"])
    def test_api2(self, a):
        logger.info("test start")
        print(f"我是{a}")
        logger.info("test over")

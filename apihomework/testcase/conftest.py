import threading
import time
import pytest


@pytest.fixture
def get_time_tag():
    # 获取时间戳
    time_tag = str(time.time()) + threading.currentThread().name
    return time_tag

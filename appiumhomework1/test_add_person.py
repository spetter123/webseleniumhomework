# 使用 Appium 实现自动化添加联系人
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWeXin:
    def setup(self):
        # 资源准备  打开应用
        caps = {"platformName": "Android",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "deviceName": "hogwarts",
                "noReset": "true",
                'skipDeviceInitialization': "true",
                "settings[waitForIdleTimeout]": 0,
                # "dontStopAppOnReset": "true"
                }
        # 提升 启动app速度的配置
        # 只有 [动态页面] 才需要设置这个 时间
        # 至关重要的一行  与appium 服务建立连接，并传递一个caps 字典对象
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待 5s 动态的等待元素出现，如果五秒 之内都没有找到元素，就会抛异常
        # 每次调用find_element/s 方法的时候都会动态的等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 资源的回收
        self.driver.quit()

    @pytest.mark.parametrize("number", {'13453288850'})
    def test_add_success(self, number):
        self.driver.find_element_by_id("com.tencent.wework:id/hc9").click()
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout"
            "/android.widget.ScrollView/android.widget.ListView/android.widget.RelativeLayout["
            "2]/android.widget.TextView").click()
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android"
            ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout"
            "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget"
            ".LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout["
            "2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout").click()
        self.driver.find_element_by_id("com.tencent.wework:id/g5f").send_keys(number)
        self.driver.find_element_by_id("com.tencent.wework:id/df9").click()
        self.driver.find_element_by_id("com.tencent.wework:id/gw").click()
        self.driver.find_element_by_id("com.tencent.wework:id/cpw").click()
        # 查找toast
        result = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '已发送')]").text
        assert "已发送" == result

    @pytest.mark.parametrize("number", {'134532888501'})
    def test_add_fail(self, number):
        self.driver.find_element_by_id("com.tencent.wework:id/hc9").click()
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout"
            "/android.widget.ScrollView/android.widget.ListView/android.widget.RelativeLayout["
            "2]/android.widget.TextView").click()
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android"
            ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout"
            "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget"
            ".LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout["
            "2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout").click()
        self.driver.find_element_by_id("com.tencent.wework:id/g5f").send_keys(number)
        self.driver.find_element_by_id("com.tencent.wework:id/df9").click()
        self.driver.find_element_by_id("com.tencent.wework:id/bg8").click()


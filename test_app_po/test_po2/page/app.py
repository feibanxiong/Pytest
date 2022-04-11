# app.py 存放app相关操作，打开，重启，关闭
import os

from appium import webdriver

from test_app_po.test_po2.page.base_page import BasePage
from test_app_po.test_po2.page.main_page import MainPage


class App(BasePage):
    def start(self):
        #udid = os.getenv('udid')
        #port = os.getenv('port')
        #复用driver：判断初始是否为None，是创建一个driver，否复用driver
        if self.driver == None:
            print("driver is None")
            #创建json串
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            #caps["udid"] = udid
            caps["ensureWebviewsHavePages"] = True
            # 下两条提升自动化测试启动速度，新设备不要添加
            caps["skipServerInstallation"] = 'true'
            caps["skipDeviceInitialization"] = 'true'
            # 客户端与服务端建立连接代码
            self.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(20)  # 隐式等待，每次调用方法都会激活
        else:

            print("driver is not None")
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        # 入口
        return MainPage(self.driver)

#app.py 存放app相关操作，打开，重启，关闭
from appium import webdriver

from test_app_po.test_po.page.main_page import MainPage


class App:
    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 下两条提升自动化测试启动速度，新设备不要添加
        caps["skipServerInstallation"] = 'true'
        caps["skipDeviceInitialization"] = 'true'
        # 客户端与服务端建立连接代码
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)  # 隐式等待，每次调用方法都会激活
        return self
    def restart(self):
        pass
    def stop(self):
        self.driver.quit()
    def goto_main(self):
        #入口
        return MainPage(self.driver)
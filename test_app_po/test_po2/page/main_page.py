from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_app_po.test_po2.page.addresslistpage import AddresslistPage
from test_app_po.test_po2.page.base_page import BasePage


class MainPage(BasePage):

    def goto_addresslist(self):
        # 点击通讯录
        self.find_and_click(By.XPATH, "//*[@text='通讯录']")
        return AddresslistPage(self.driver)

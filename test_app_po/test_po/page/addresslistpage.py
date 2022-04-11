from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_app_po.test_po.page.addmemberpage import AddMemberPage
from test_app_po.test_po.page.base_page import BasePage


class AddresslistPage(BasePage):

    def goto_addmember(self):
        # 点击添加成员
        self.find_and_click(By.XPATH, "//*[@text='添加成员']")
        return AddMemberPage(self.driver)

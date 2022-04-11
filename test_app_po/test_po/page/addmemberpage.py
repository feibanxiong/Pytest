from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_app_po.test_po.page.base_page import BasePage


class AddMemberPage(BasePage):

    def click_addmember_menual(self):
        # 点击手动输入添加
        from test_app_po.test_po.page.editmemberpage import EditMemberPage
        self.find_and_click(By.XPATH, "//*[@text='手动输入添加']")

        return EditMemberPage(self.driver)

    def get_tip(self):
        result = self.find(By.XPATH, "//*[@class='android.widget.Toast']").get_attribute("text")
        return result

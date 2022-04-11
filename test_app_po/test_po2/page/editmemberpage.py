from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_app_po.test_po2.page.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phone_num):
        """
        input 姓名
        input 手机号
        click 保存
        """
        from test_app_po.test_po2.page.addmemberpage import AddMemberPage

        self.find_and_send(By.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText", name)
        self.find_and_send(By.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText", phone_num)
        # //*[contains(@text, '手机')]/..//*[@text='必填']
        self.find_and_click(By.XPATH, "//*[@text='保存']")
        return AddMemberPage(self.driver)

# 完成基本内容的封装，例如初始化driver，find，find and click
import logging

from appium.webdriver.webdriver import WebDriver

logger = logging.getLogger()


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, value):
        logger.info('find')
        logger.info(by)
        logger.info(value)

        return self.driver.find_element(by, value)

    def find_and_click(self, by, value):
        logger.info('find_and_click')
        logger.info(by)
        logger.info(value)
        self.find(by, value).click()

    def find_and_send(self, by, value, text):
        logger.info('find_and_send')
        logger.info(by)
        logger.info(value)
        logger.info(text)
        self.find(by, value).send_keys(text)

    def back(self, num=3):
        logger.info('back')
        for i in range(0, num):
            self.driver.back()

import logging
import allure

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    BASE_URL = 'http://testshop.qa-practice.com/shop'
    PAGE_URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def open_page(self):
        logging.info(f'Переходим на страницу {self.BASE_URL}{self.PAGE_URL}')
        with allure.step(f'Переходим на страницу {self.BASE_URL}{self.PAGE_URL}'):
            return self.driver.get(f'{self.BASE_URL}{self.PAGE_URL}')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

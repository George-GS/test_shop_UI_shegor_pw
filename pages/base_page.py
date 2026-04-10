import logging
import allure

from playwright.sync_api import Page


class BasePage:
    BASE_URL = 'http://testshop.qa-practice.com/shop'
    PAGE_URL = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        logging.info(f'Переходим на страницу {self.BASE_URL}{self.PAGE_URL}')
        with allure.step(f'Переходим на страницу {self.BASE_URL}{self.PAGE_URL}'):
            return self.page.goto(f'{self.BASE_URL}{self.PAGE_URL}')

    def find(self, locator: tuple):
        return self.page.locator(locator)

    def find_all(self, locator: tuple):
        return self.page.locator(locator).all()

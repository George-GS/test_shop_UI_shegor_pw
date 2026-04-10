import logging
import allure

from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators import cart_page_locators as loc


class CartPage(BasePage):
    PAGE_URL = '/cart'

    def check_product_in_cart(self, product_name):
        logging.info(f'Проверяем, что товар "{product_name}" есть в корзине')
        with allure.step(f'Проверяем наличие товара "{product_name}" в корзине'):
            expect(self.find(loc.product_in_cart)).to_have_text(product_name)

    def check_cart_header(self):
        logging.info('Проверяем заголовок страницы корзины')
        with allure.step('Проверяем заголовок "Order overview"'):
            expect(self.find(loc.cart_header), 'Нет заголовка "Order overview"').to_have_text('Order overview')

    def check_cart_is_empty(self):
        logging.info('Проверяем, что корзина пуста')
        with allure.step('Проверяем, что корзина пуста'):
            expect(self.find(loc.empty_cart_info),
                   'Нет информации о том, что корзина пуста').to_have_text('Your cart is empty!')

    def remove_product(self):
        logging.info('Удаляем товар из корзины')
        with allure.step('Удаляем товар из корзины'):
            remove_btn = self.find(loc.remove_btn)
            remove_btn.click()
            expect(self.find(loc.product_in_cart)).to_be_visible()

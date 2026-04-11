import logging
import allure

from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators import product_page_locators as loc


class ProductPage(BasePage):
    PAGE_URL = '/furn-9999-office-design-software-7?category=9'

    def check_name(self, expected_name):
        logging.info(f'Проверяем название товара. Ожидается: "{expected_name}"')
        with allure.step(f'Проверяем название товара (ожидается "{expected_name}")'):
            actual_name = self.find(loc.name_product_loc)
            expect(actual_name,
                   f'Ожидаемое имя: {expected_name}, текущее имя: {actual_name}').to_have_text(expected_name)

    def check_price(self, expected_price):
        logging.info(f'Проверяем цену товара. Ожидается: "{expected_price}"')
        with allure.step(f'Проверяем цену товара (ожидается "{expected_price}")'):
            actual__price = self.find(loc.price_product_loc)
            expect(actual__price,
                   f'Ожидаемое имя: {expected_price}, текущее имя: { actual__price}').to_have_text(expected_price)

    def check_image(self):
        logging.info('Проверяем наличие изображения товара')
        with allure.step('Проверяем наличие изображения товара'):
            image_product = self.page.locator(loc.image_product_loc)
            src = image_product.get_attribute("src")
            assert src, "Атрибут src отсутствует или пуст"

    def add_plus_one(self):
        logging.info('Увеличиваем количество товара на 1')
        with allure.step('Увеличиваем количество товара в корзине на 1'):
            self.find(loc.add_one).click()

    def add_to_cart(self):
        logging.info('Добавляем товар в корзину')
        with allure.step('Нажимаем кнопку "Add to cart"'):
            self.find(loc.add_to_cart).click()

    def verify_added_to_cart_notification(self, expected_text):
        logging.info(f'Проверяем уведомление о добавлении в корзину: "{expected_text}"')
        with allure.step(f'Проверяем уведомление о добавлении в корзину'):
            product_in_cart_notif = self.find(loc.product_name_in_cart_loc)
            expect(product_in_cart_notif,
                   f'Ожидалось: {expected_text}. Текущее: {product_in_cart_notif.inner_text()}').to_have_text(expected_text)

    def change_currency_to_euro(self):
        logging.info('Меняем валюту на евро')
        with allure.step('Переключаем валюту на евро'):
            currency = self.find(loc.currency_loc)
            currency.click()
            eur = self.find(loc.eur_loc)
            eur.click()

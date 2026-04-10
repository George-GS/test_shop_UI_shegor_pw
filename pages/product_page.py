import logging
import allure

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import product_page_locators as loc


class ProductPage(BasePage):
    PAGE_URL = '/furn-9999-office-design-software-7?category=9'

    def check_name(self, expected_name):
        logging.info(f'Проверяем название товара. Ожидается: "{expected_name}"')
        with allure.step(f'Проверяем название товара (ожидается "{expected_name}")'):
            actual_name = self.find(loc.name_product_loc)
            assert actual_name.text == expected_name, f'Неверное имя товара. ' \
                                             f'Ожидаемое имя: {expected_name}, текущее имя: {actual_name}'

    def check_price(self, expected_price):
        logging.info(f'Проверяем цену товара. Ожидается: "{expected_price}"')
        with allure.step(f'Проверяем цену товара (ожидается "{expected_price}")'):
            actual__price = self.find(loc.price_product_loc)
            assert actual__price.text == expected_price, \
                f'Неверная цена товара. Ожидаемая цена: {expected_price}, текущая цена: {actual__price}'

    def check_image(self):
        logging.info('Проверяем наличие изображения товара')
        with allure.step('Проверяем наличие изображения товара'):
            image_product = self.wait.until(EC.visibility_of_element_located(loc.image_product_loc))
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
            product_in_cart_notification = self.wait.until(EC.visibility_of_element_located(loc.product_name_in_cart_loc))
            assert product_in_cart_notification.text == expected_text, f'Ожидалось: {expected_text}. \n' \
                                                                       f'Текущее: {product_in_cart_notification.text}'

    def change_currency_to_euro(self):
        logging.info('Меняем валюту на евро')
        with allure.step('Переключаем валюту на евро'):
            currency = self.find(loc.currency_loc)
            currency.click()
            eur = self.wait.until(EC.element_to_be_clickable(loc.eur_loc))
            eur.click()

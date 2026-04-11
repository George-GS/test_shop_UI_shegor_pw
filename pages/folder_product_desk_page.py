import logging
import allure

from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators import folder_product_desk_locators as loc
from time import sleep


class FolderProductDeskPage(BasePage):
    PAGE_URL = '/category/desks-1'

    def products_displayed_on_page(self):
        logging.info(f'Проверяем, что на странице {self.PAGE_URL} есть товары')
        with allure.step(f'Проверяем наличие товаров на странице'):
            count_product = self.get_visible_products_count_static()
            assert count_product > 0, f'На странице {self.PAGE_URL} нет товаров'

    def search_product(self, product_name):
        logging.info(f'Вводим в поиск: "{product_name}"')
        with allure.step(f'Вводим в поиск "{product_name}"'):
            search_field = self.page.get_by_role(**loc.search_loc)
            search_field.fill(product_name)
            search_field.press('Enter')
            self.page.wait_for_load_state('networkidle')
            return self

    def get_visible_products_count_after_action(self):
        self.page.wait_for_load_state('networkidle')
        products_count = self.find_all(loc.visible_products_loc)
        return len(products_count)

    def get_visible_products_count_static(self):
        products_count = self.find_all(loc.visible_products_loc)
        return len(products_count)

    def verify_products_count(self, expected_count):
        logging.info(f'Проверяем количество товаров. Ожидается: {expected_count}')
        with allure.step(f'Проверяем количество товаров (ожидается {expected_count})'):
            actual_count = self.get_visible_products_count_after_action()
            assert actual_count == expected_count, \
                f'Ожидалось количество товаров {expected_count}, отображается товаров {actual_count}'
            return self

    def verify_product_in_results(self, product_name):
        logging.info(f'Проверяем, что товар "{product_name}" есть в результатах')
        with allure.step(f'Проверяем наличие товара "{product_name}" в результатах'):
            product_name_in_result = self.page.get_by_role(**loc.product_name_loc)
            expect(product_name_in_result, f'В результатах нет товара {product_name}').to_have_text(product_name)

    def check_product_not_exist(self, product_name):
        logging.info(f'Проверяем сообщение об отсутствии товара "{product_name}"')
        with allure.step(f'Проверяем сообщение об отсутствии товара "{product_name}"'):
            actual_text_no_result = self.page.locator(loc.no_result)
            expected_text_no_result = 'No results'
            actual_text_no_result_with_product = self.page.locator(loc.no_result_with_product)
            expected_text_no_result_with_product = f'No results for "{product_name}" in category "Desks".'
            expect(actual_text_no_result,
                   f'Ожидался текст: {expected_text_no_result}').to_have_text(expected_text_no_result)
            expect(actual_text_no_result_with_product,
                   f'Ожидался текст: {expected_text_no_result_with_product}').to_have_text(expected_text_no_result_with_product)

    def select_checkbox_filter_aluminium(self):
        logging.info('Выбираем фильтр "Алюминий"')
        with allure.step('Выбираем фильтр "Алюминий"'):
            sleep(1)
            self.find(loc.checkbox_aluminium).first.click()
            self.page.wait_for_load_state('networkidle')

    def add_to_cart_hover(self):
        logging.info('Наводим курсор на товар и добавляем в корзину')
        with allure.step('Наводим курсор на товар и добавляем в корзину'):
            product_table = self.page.locator(loc.product_table)
            product_table.hover()
            self.page.get_by_role(**loc.cart_btn).first.click()

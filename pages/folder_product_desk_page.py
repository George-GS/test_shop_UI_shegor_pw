import logging
import allure

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import folder_product_desk_locators as loc


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
            search_field = self.find(loc.search_loc)
            search_field.send_keys(product_name)
            search_field.send_keys(Keys.ENTER)
            return self

    def get_visible_products_count_after_action(self):
        self.wait.until(EC.url_changes(f'{self.BASE_URL}{self.PAGE_URL}'))
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
            product_in_result = self.find(loc.visible_products_loc)
            assert 'Customizable Desk' in product_in_result.text, f'В результатах нет товара {product_name}'

    def check_product_not_exist(self, product_name):
        logging.info(f'Проверяем сообщение об отсутствии товара "{product_name}"')
        with allure.step(f'Проверяем сообщение об отсутствии товара "{product_name}"'):
            actual_text_no_result = self.wait.until(EC.presence_of_element_located(loc.no_result)).text
            expected_text_no_result = 'No results'
            actual_text_no_result_with_product = self.wait.until(EC.presence_of_element_located(
                loc.no_result_with_product)).text
            expected_text_no_result_with_product = f'No results for "{product_name}" in category "Desks".'
            assert actual_text_no_result == expected_text_no_result, \
                f'Ожидался текст: {expected_text_no_result}, текущий текст: {actual_text_no_result}'
            assert actual_text_no_result_with_product == expected_text_no_result_with_product, \
                f'Ожидался текст: {expected_text_no_result_with_product}, текущий текст: {actual_text_no_result_with_product}'

    def select_checkbox_filter_aluminium(self):
        logging.info('Выбираем фильтр "Алюминий"')
        with allure.step('Выбираем фильтр "Алюминий"'):
            self.wait.until(EC.visibility_of_element_located(loc.sss))
            checkbox_filter = self.wait.until(EC.element_to_be_clickable(loc.checkbox_aluminium))
            checkbox_filter.click()

    def add_to_cart_hover(self):
        logging.info('Наводим курсор на товар и добавляем в корзину')
        with allure.step('Наводим курсор на товар и добавляем в корзину'):
            product_table = self.wait.until(EC.visibility_of_element_located(loc.product_table))
            self.action.move_to_element(product_table).perform()
            self.wait.until(EC.element_to_be_clickable(loc.cart_btn)).click()

import pytest
import allure


@allure.title('Проверка данных товара: название, цена, изображение')
def test_check_product_data(product_page):
    product_page.open_page()
    product_page.check_name()
    product_page.check_price()
    product_page.check_image()


@allure.title('Добавление товара в корзину через страницу товара с изменением количества')
def test_add_to_cart_from_product_page(product_page, cart_modal_window):
    count = 2
    product_page.open_page()
    name = product_page.get_prod_name()
    product_page.add_plus_one()
    product_page.add_to_cart()
    cart_modal_window.continue_shopping()
    product_page.verify_added_to_cart_notification(count, name)


@allure.title('Изменение валюты на Евро на странице товара')
def test_change_currency_on_product_page(product_page):
    product_page.open_page()
    product_page.change_currency_to_euro()
    product_page.check_price_euro()

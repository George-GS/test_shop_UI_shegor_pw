import pytest
import allure


@allure.title('Проверка данных товара: название, цена, изображение')
def test_check_product_data(product_page):
    product_name = 'Office Design Software'
    product_price = '$ 280.00'
    product_page.open_page()
    product_page.check_name(product_name)
    product_page.check_price(product_price)
    product_page.check_image()


@allure.title('Добавление товара в корзину через страницу товара с изменением количества')
def test_add_to_cart_from_product_page(product_page):
    count_and_name = '2 x Office Design Software'
    product_page.open_page()
    product_page.add_plus_one()
    product_page.add_to_cart()
    product_page.verify_added_to_cart_notification(count_and_name)


@allure.title('Изменение валюты на Евро на странице товара')
def test_change_currency_on_product_page(product_page):
    expected_price = '359.35 €'
    product_page.open_page()
    product_page.change_currency_to_euro()
    product_page.check_price(expected_price)

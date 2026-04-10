import pytest
import allure


@allure.title('Проверка наличия добавленного товара в корзине')
def test_check_product_in_cart(cart_with_product):
    product_name = 'Customizable Desk'
    cart_with_product.check_product_in_cart(product_name)


@allure.title('Проверка отображения пустой корзины')
def test_empty_cart(cart_page):
    cart_page.open_page()
    cart_page.check_cart_header()
    cart_page.check_cart_is_empty()


@allure.title('Проверка удаления товара из корзины')
def test_remove_product(cart_with_product):
    product_name = 'Customizable Desk'
    cart_with_product.check_product_in_cart(product_name)
    cart_with_product.remove_product()
    cart_with_product.check_cart_is_empty()

import pytest
import allure


@allure.title('Проверка отображения товаров на странице раздела товаров')
def test_products_displayed_on_page(folder_product_desk_page):
    folder_product_desk_page.open_page()
    folder_product_desk_page.products_displayed_on_page()


@allure.title('Поиск существующего товара на странице раздела товаров')
def test_search_existing_product(folder_product_desk_page):
    product_name = 'Customizable Desk'
    folder_product_desk_page.open_page()
    folder_product_desk_page.search_product(product_name)
    folder_product_desk_page.verify_products_count(1)
    folder_product_desk_page.verify_product_in_results(product_name)


@allure.title('Поиск несуществующего товара на странице раздела товаров')
def test_search_nonexisten_product(folder_product_desk_page):
    product_name = 'not exist'
    folder_product_desk_page.open_page()
    folder_product_desk_page.search_product(product_name)
    folder_product_desk_page.verify_products_count(0)
    folder_product_desk_page.check_product_not_exist(product_name)


@allure.title('Фильтрация товаров по материалу')
def test_filter_by_aluminium(folder_product_desk_page):
    product_name = 'Customizable Desk'
    folder_product_desk_page.open_page()
    folder_product_desk_page.select_checkbox_filter_aluminium()
    folder_product_desk_page.verify_products_count(1)
    folder_product_desk_page.verify_product_in_results(product_name)

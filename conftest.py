import pytest

from playwright.sync_api import Page, BrowserContext, expect

from pages.folder_product_desk_page import FolderProductDeskPage
from pages.cart_page import CartPage
from pages.cart_modal_window import CartModalWindow
from pages.product_page import ProductPage


@pytest.fixture()
def page(context: BrowserContext, playwright) -> Page:
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def folder_product_desk_page(page):
    return FolderProductDeskPage(page)


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def cart_modal_window(page):
    return CartModalWindow(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def cart_with_product(page, folder_product_desk_page, cart_modal_window, cart_page):
    folder_product_desk_page.open_page()
    folder_product_desk_page.add_to_cart_hover()
    cart_modal_window.go_to_cart()
    return cart_page

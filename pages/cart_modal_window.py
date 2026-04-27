import logging
import allure

from pages.base_page import BasePage
from pages.locators import cart_modal_window_locators as loc


class CartModalWindow(BasePage):

    def go_to_cart(self):
        logging.info('Переходим в корзину через модальное окно')
        with allure.step('Нажимаем кнопку перехода в корзину'):
            self.page.locator(loc.btn_proceed_to_checkout).click()
            self.page.wait_for_url('**/cart')

    def continue_shopping(self):
        logging.info('В модальном окне нажимаем кнопку "Продолжить покупки"')
        with allure.step('В модальном окне нажимаем кнопку "Продолжить покупки"'):
            self.page.locator(loc.btn_continue_shopping).click()



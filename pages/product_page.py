from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_message_about_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ITEM), "Message about item in cart is not " \
                                                                                 "presented "

    def should_be_message_about_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), "Message about price in cart is not " \
                                                                            "presented "

    def text_in_message_about_add_to_cart(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_name_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ITEM).text
        assert item_name == item_name_in_message, f"expected item_name is '{item_name}', but u got'{item_name_in_message}' "

    def price_in_message_about_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_cart = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert price in price_in_cart, f"expected item_cost is '{price}', but u got in cart'{price_in_cart}' "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

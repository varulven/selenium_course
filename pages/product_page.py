from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_message_about_add_to_cart(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_name_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ITEM).text
        assert item_name == item_name_in_message, f"expected item_name is '{item_name}', but u got'{item_name_in_message}' "

    def should_be_message_about_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_cart = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert price in price_in_cart, f"expected item_cost is '{price}', but u got in card'{price_in_cart}' "

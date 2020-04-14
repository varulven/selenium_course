from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_message_about_add_to_cart(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        item_name_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ITEM)
        assert item_name.text in item_name_in_message.text, f"expected item_name is '{item_name.text}', but u got'{item_name_in_message.text}' "

    def should_be_message_about_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_in_cart = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
        assert price.text in price_in_cart.text, f"expected item_cost is '{price.text}', but u got in card'{price_in_cart.text}' "
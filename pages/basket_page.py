from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def cart_has_no_items(self):
        cart_message = self.browser.find_element(*BasketPageLocators.CART_MESSAGE).text
        en_cart_message = "Your basket is empty"
        ru_cart_message = "Ваша корзина пуста"
        assert en_cart_message in cart_message, f"expected '{en_cart_message}' contains in '{cart_message}' "

    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_CART), \
            "Some items in card is presented, but should not be"

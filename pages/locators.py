from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ITEM = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    # MESSAGE_ABOUT_ITEM2 = (By.CSS_SELECTOR, ".alert-success:nth-child(2) strong")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    # FOR_TEST = (By.CSS_SELECTOR, ".instock")
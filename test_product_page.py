import time
import os
import pytest
from .pages.product_page import ProductPage

link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link3 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='nobody wants to fix this bug')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # выполняем метод страницы
    # login_page = page.go_to_login_page()
    # time.sleep(2)
    page.solve_quiz_and_get_code()
    # time.sleep(2)
    page.should_be_message_about_add_to_cart()
    page.should_be_message_about_price()
    page.text_in_message_about_add_to_cart()
    page.price_in_message_about_price()

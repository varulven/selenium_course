import time
import os
import pytest
from .pages.product_page import ProductPage

link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link3 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_can_add_product_to_basket(browser):
    # link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,
                       link3)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # выполняем метод страницы
    # time.sleep(2)
    page.solve_quiz_and_get_code()
    # time.sleep(2)
    page.should_be_message_about_add_to_cart()
    page.should_be_message_about_price()
    page.text_in_message_about_add_to_cart()
    page.price_in_message_about_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser,
                       link3)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser,
                       link3)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser,
                       link3)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()
    page.should_disappeared_success_message()

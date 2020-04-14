import time
import os
import pytest
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.add_to_cart()                  # выполняем метод страницы
    # login_page = page.go_to_login_page()
    #time.sleep(2)
    page.solve_quiz_and_get_code()
    #time.sleep(2)
    page.should_be_message_about_add_to_cart()
    page.should_be_message_about_price()

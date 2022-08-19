import pytest
from .pages.product_page import ProductPage
import time

base_url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'


# тест для проверки добавления товара в корзину
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.check_product_added_to_cart()
    page.check_product_price()
    # page.should_disappear_success_message() проверка, что сообщение исчезает
    # page.should_not_be_success_message() проверка, что сообщение об успешном добавлении в корзину не появляется

# тест с багом по ссылке + помечаем баг как xfail
@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='bugged_link')) for i in range(10)])
def test_promo_page(browser, promo_offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.check_product_added_to_cart()
    page.check_product_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.add_to_cart_button()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_url)
    page.open()
    page.add_to_cart_button()
    page.should_disappear_success_message()

@pytest.mark.smoke
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.smoke
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
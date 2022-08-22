import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
        page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.should_be_login_url()
        login_page.should_be_login_form()
        login_page.should_be_register_form()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_into_cart()
        page.should_not_be_item_in_cart()
        page.should_be_empty_cart_text()









from .base_page import BasePage
from .locators import (MainPageLocators, LoginPageLocators)


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM)

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'The "login" in url was not found'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
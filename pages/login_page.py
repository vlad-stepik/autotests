from .base_page import BasePage
from .locators import (MainPageLocators, BasePageLocators, LoginPageLocators)


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM)

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'The "login" in url was not found'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        password_field_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_FIELD)
        password_field_repeat.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON).click()


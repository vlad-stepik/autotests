from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
       assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


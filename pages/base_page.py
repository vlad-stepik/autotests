from selenium.common.exceptions import (NoSuchElementException, NoAlertPresentException, TimeoutException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import (BasePageLocators, MainPageLocators, CartPageLocators, LoginPageLocators)
import math

class BasePage():

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    # Т.к. изначально создали: self.browser = browser и self.url = url,
    # то в своей функции обращаемся также к self.browser и self.url
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def go_into_cart(self):
        self.browser.find_element(*MainPageLocators.CART_BUTTON).click()

    def should_not_be_item_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEM), 'Cart item is presented'

    def should_be_empty_cart_text(self):
        assert self.browser.find_element(*CartPageLocators.CART_ITEM_EMPTY_TEXT), 'Text about empty cart is missing'


    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # когда хотим проверить, что элемент исчезает на странице
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # когда хотим проверить, что элемент не появляется на странице после какого-то действия
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


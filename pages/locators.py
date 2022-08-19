from selenium.webdriver.common.by import By

class MainPageLocators():
    pass

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main p.price_color')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')
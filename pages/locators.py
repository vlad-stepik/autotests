from selenium.webdriver.common.by import By

class MainPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, 'span.btn-group a.btn.btn-default')

class CartPageLocators():
    CART_ITEM = (By.CSS_SELECTOR, 'div.basket-items')
    CART_ITEM_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_FIELD = (By.NAME, 'registration-email')
    PASSWORD_FIELD = (By.NAME, 'registration-password1')
    PASSWORD_REPEAT_FIELD = (By.NAME, 'registration-password2')
    REGISTER_FORM_BUTTON = (By.NAME, 'registration_submit')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main p.price_color')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')
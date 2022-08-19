from .locators import CartPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def items_are_missing_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEM), 'Cart item is presented'

    def should_be_text_about_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.CART_ITEM_EMPTY_TEXT), 'Text about empty cart is missing'
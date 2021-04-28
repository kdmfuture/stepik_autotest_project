from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert not self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_ELEMENT)

    def empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT_ELEMENT)
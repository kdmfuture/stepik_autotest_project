from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def check_names(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ELEMENT)
        list_of_elements = self.browser.find_elements(*ProductPageLocators.LIST_OF_ELEMENTS)
        list_of_texts = []
        for elem in list_of_elements:
            list_of_texts.append(elem.text)
        assert book_name.text in list_of_texts

    def compare_prices(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_ELEMENT)
        basket_elements = self.browser.find_elements(*ProductPageLocators.BASKET_ELEMENTS)
        basket_price = []
        for elem in basket_elements:
            basket_price.append(elem.text)
        assert price.text in basket_price

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


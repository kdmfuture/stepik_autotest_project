from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def check_names(self):
        book_name = self.browser.find_element_by_xpath("//h1")
        list_of_elements = self.browser.find_elements_by_xpath("//div/strong")
        list_of_texts = []
        for elem in list_of_elements:
            list_of_texts.append(elem.text)
        assert book_name.text in list_of_texts

    def compare_prices(self):
        price = self.browser.find_element_by_xpath("//p[@class=\"price_color\"]")
        basket_elements = self.browser.find_elements_by_xpath("//div/p/strong")
        basket_price = []
        for elem in basket_elements:
            basket_price.append(elem.text)
        assert price.text in basket_price


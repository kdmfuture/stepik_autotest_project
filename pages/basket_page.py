from selenium.webdriver.common.by import By

from .base_page import BasePage


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert not self.is_not_element_present(By.XPATH, "//p/a")

    def empty_basket_text(self):
        assert self.is_element_present(By.XPATH, "//p[contains(.,\"empty\")]")
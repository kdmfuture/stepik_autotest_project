from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link ")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, "//button[@class=\"btn btn-lg btn-primary btn-add-to-basket\"]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class=\"alertinner \" and contains(., \" has been added\")]")


from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link ")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")
    BASKET_BUTTON = (By.XPATH, "//a[@class=\"btn btn-default\"]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.XPATH, "//form[@id=\"register_form\"]//input[@type=\"email\"]")
    REGISTER_PASSWORD1 = (By.XPATH, "//form[@id=\"register_form\"]//input[@name=\"registration-password1\"]")
    REGISTER_PASSWORD2 = (By.XPATH, "//form[@id=\"register_form\"]//input[@name=\"registration-password2\"]")
    REGISTER_BUTTON = (By.XPATH, "//button[@name=\"registration_submit\"]")


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, "//button[@class=\"btn btn-lg btn-primary btn-add-to-basket\"]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class=\"alertinner \" and contains(., \" has been added\")]")
    BOOK_NAME_ELEMENT = (By.XPATH, "//h1")
    LIST_OF_ELEMENTS = (By.XPATH, "//div/strong")
    PRICE_ELEMENT = (By.XPATH, "//p[@class=\"price_color\"]")
    BASKET_ELEMENTS = (By.XPATH, "//div/p/strong")


class BasketPageLocators:
    EMPTY_BASKET_ELEMENT = (By.XPATH, "//p/a")
    EMPTY_BASKET_TEXT_ELEMENT = (By.XPATH, "//p[contains(.,\"empty\")]")
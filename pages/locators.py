from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_IN = (By.ID, "login_form")
    REGISTER = (By.ID, "register_form")
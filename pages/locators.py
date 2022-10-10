from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'login')]")
    USER_ICON = (By.CSS_SELECTOR, "[data-analytics-event*='icon:avatar']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login")
    LOGIN_FIELD = (By.CSS_SELECTOR, "#login_field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "input[data-signin-label='Sign in']")

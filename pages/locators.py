from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'login')]")
    USER_ICON = (By.CSS_SELECTOR, "[data-analytics-event*='icon:avatar']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login")
    LOGIN_FIELD = (By.CSS_SELECTOR, "#login_field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "input[data-signin-label='Sign in']")


class MainAuthenticationUserPageLocators():
    # REPOSITORY_NAME_FIELD = (By.CSS_SELECTOR, '#new_repository input[aria-label="repository name"]')
    # PUBLIC_REPOSITORY = (By.CSS_SELECTOR, '#new_repository input[value="public"]')
    # PRIVAT_REPOSITORY = (By.CSS_SELECTOR, '#new_repository input[value="private"]')
    CREATE_NEW_REPOSITORY_BUTTON = (By.CSS_SELECTOR, 'aside[aria-label="Account"] a[href="/new"]')


class NewRepositoryPageLocators():
    NAME_NEW_REPOSITORY = (By.CSS_SELECTOR, "#repository_name")
    BUTTON_CREATE_REPOSITORY = (By.CSS_SELECTOR, "button[data-disable-with='Creating repository&hellip;']")

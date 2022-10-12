from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'login')]")
    USER_ICON = (By.CSS_SELECTOR, "[data-analytics-event*='icon:avatar']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login")
    LOGIN_FIELD = (By.CSS_SELECTOR, "#login_field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "input[data-signin-label='Sign in']")


class MainUserPageLocators():
    # REPOSITORY_NAME_FIELD = (By.CSS_SELECTOR, '#new_repository input[aria-label="repository name"]')
    # PUBLIC_REPOSITORY = (By.CSS_SELECTOR, '#new_repository input[value="public"]')
    # PRIVAT_REPOSITORY = (By.CSS_SELECTOR, '#new_repository input[value="private"]')
    CREATE_NEW_REPOSITORY_BUTTON = (By.CSS_SELECTOR, 'aside[aria-label="Account"] a[href="/new"]')
    REPOSITORY_LINK = (By.CSS_SELECTOR, 'aside ul li a.markdown-title')


class NewRepositoryPageLocators():
    NAME_NEW_REPOSITORY = (By.CSS_SELECTOR, "#repository_name")
    BUTTON_CREATE_REPOSITORY = (By.CSS_SELECTOR, "button[data-disable-with='Creating repository&hellip;']")


class RepositoryPageLocators():
    SETTING_REPOSITORY_TAB = (By.CSS_SELECTOR, '#settings-tab')


class RepositorySettingPageLocators():
    BUTTON_DELETE_REPOSITORY = (By.XPATH, "//summary['text()=Delete this repository']")
    RENAME_FIELD = (By.CSS_SELECTOR, "#rename-field")
    RENAME_BUTTON = (By.CSS_SELECTOR, "form.d-flex button")

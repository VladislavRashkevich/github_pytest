from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'login')]")
    USER_ICON = (By.CSS_SELECTOR, "[data-analytics-event*='icon:avatar']")


class LoginPageLocators():
    LOGIN_FORM_WEB_ELEMENT = (By.CSS_SELECTOR, "#login")
    LOGIN_FIELD = (By.CSS_SELECTOR, "#login_field")  # '#err')
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "input[data-signin-label='Sign in']")


class MainUserPageLocators():
    CREATE_NEW_REPOSITORY_BUTTON = (By.CSS_SELECTOR, 'aside[aria-label="Account"] a[href="/new"]')
    REPOSITORY_LINK = (By.CSS_SELECTOR, 'aside ul li a.markdown-title')


class NewRepositoryPageLocators():
    NAME_NEW_REPOSITORY = (By.CSS_SELECTOR, "#repository_name")
    BUTTON_CREATE_REPOSITORY = (By.CSS_SELECTOR, "button[data-disable-with='Creating repository&hellip;']")


class ReadmePageLocators():
    MAIN_README_FIELD = (By.CSS_SELECTOR, 'textarea[data-hotkey-scope-id="code-editor"]')
    COMMIT_TITLE_FIELD = (By.CSS_SELECTOR, '#commit-summary-input')
    COMMIT_DESCRIPTION_FIELD = (By.CSS_SELECTOR, '#commit-description-textarea')
    SUBMIT_FILE_BUTTON = (By.CSS_SELECTOR, '#submit-file')


class RepositoryPageLocators():
    SETTING_REPOSITORY_TAB = (By.CSS_SELECTOR, '#settings-tab')
    LINK_EMPTY_README = (By.CSS_SELECTOR, "a[data-ga-click*='Clicked README link']")
    FILE_IN_REPOSITORY = (By.CSS_SELECTOR, 'div[aria-labelledby="files"] a.Link--primary')


class RepositorySettingPageLocators():
    RENAME_FIELD = (By.CSS_SELECTOR, "#rename-field")
    RENAME_BUTTON = (By.CSS_SELECTOR, "form.d-flex button")

    DELETE_REPOSITORY_BUTTON = (By.XPATH, "//li//summary[contains(text(), 'Delete this repository')]")

    CONFIRMATION_STRING_TO_DELETE_REPOSITORY = (By.CSS_SELECTOR, 'details-dialog[aria-label="Delete repository"] p:nth-child(2) strong')
    CONFIRMATION_FIELD_TO_DELETE_REPOSITORY = (By.CSS_SELECTOR, 'details-dialog[aria-label="Delete repository"] p input')
    CONFIRMATION_BUTTON_TO_DELETE_REPOSITORY = (By.CSS_SELECTOR, 'details-dialog[aria-label="Delete repository"] form button')

    CONFIRMATION_ASSERT_PASSWORD_FIELD = (By.CSS_SELECTOR, '#sudo_password')
    CONFIRMATION_ACCESS_BUTTON = (By.XPATH, '//button[contains(text(), "Confirm")]')

    MESSAGE_REPOSITORY_EMPTY = (By.CSS_SELECTOR, "#user-repositories-list h2")
import allure
from .locators import BasePageLocators
from test_first_task.utilits.browser_helper import BrowserHelper


class BasePage():

    base_locators = BasePageLocators

    def __init__(self, browser, url, browser_helper=BrowserHelper):
        self.url = url
        self.browser = browser
        self.browser_helper = browser_helper(self.browser)

    @allure.step("Open page")
    def open(self):
        self.browser.get(self.url)

    @allure.step("Open login page")
    def go_to_login_page(self):
        login_link = self.browser_helper.element_is_clickable(self.base_locators.LOGIN_LINK)
        login_link.click()

    @allure.step("User authorization verification")
    def should_be_authorized_user(self):
        res = self.browser_helper.element_is_visible(self.base_locators.USER_ICON)
        # if not res:
        #     allure.attach(
        #         self.browser.get_screenshot_as_png(),
        #         name="authorization bug",
        #         attachment_type=allure.attachment_type.PNG
        #     )
        assert res, "User is not authorized"

    @allure.step("Verification for a link to the login page")
    def should_be_login_link(self):
        assert self.browser_helper.element_is_visible(self.base_locators.LOGIN_LINK), "Login link is not present in page"

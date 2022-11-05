import allure
from .base_page import BasePage
from .locators import MainUserPageLocators


class MainUserPage(BasePage):
    locators = MainUserPageLocators

    @allure.step('Open page to create new repository')
    def go_to_page_for_create_new_repository(self):
        new_button = self.browser_helper.element_is_clickable(self.locators.CREATE_NEW_REPOSITORY_BUTTON)
        new_button.click()

    @allure.step('Open repository page')
    def go_to_repository_page(self):
        repository_link = self.browser_helper.element_is_clickable(self.locators.REPOSITORY_LINK)
        repository_link.click()


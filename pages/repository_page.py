import allure
from .base_page import BasePage
from .locators import RepositoryPageLocators


class RepositoryPage(BasePage):

    locators = RepositoryPageLocators

    @allure.step('Go to repository setting')
    def go_to_repository_setting(self):
        setting_tab = self.browser_helper.element_is_clickable(self.locators.SETTING_REPOSITORY_TAB)
        setting_tab.click()

    @allure.step('Go to new readme page')
    def go_to_new_readme_page(self):
        link_empty_readme = self.browser_helper.element_is_visible(self.locators.LINK_EMPTY_README)
        link_empty_readme.click()



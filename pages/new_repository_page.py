import allure
from .base_page import BasePage
from .locators import NewRepositoryPageLocators


class NewRepositoryPage(BasePage):
    locators = NewRepositoryPageLocators

    @allure.step('Add name repository')
    def add_name_repository(self, name_new_repository):
        """Add name repository"""
        name_place = self.browser_helper.element_is_visible(self.locators.NAME_NEW_REPOSITORY)
        self.browser_helper.send_keys_in_element(name_place, name_new_repository)

    @allure.step('Create repository')
    def create_repository(self):
        """Create repository"""
        button_create_repository = self.browser_helper.element_is_clickable(self.locators.BUTTON_CREATE_REPOSITORY)
        button_create_repository.click()

    @allure.step('Create new repository')
    def create_new_repository(self, name_new_repository: str = "repository_test"):
        """Create new repository"""
        self.add_name_repository(name_new_repository)
        self.create_repository()

    @allure.step('Verification repository is create')
    def new_repo_should_be_created(self, name_new_repository: str):
        """'Verification repository is create'"""
        assert name_new_repository in self.browser.current_url, "New repository was not create"

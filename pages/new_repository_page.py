import allure

from .base_page import BasePage
from .locators import NewRepositoryPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NewRepositoryPage(BasePage):

    @allure.step('Create new repository')
    def create_new_repository(self, name_new_repository: str = "repository_test"):
        """Создаем новый репозиторий"""
        self.add_name_repository(name_new_repository)
        self.create_repository()

    @allure.step('Add name repository')
    def add_name_repository(self, name_new_repository):
        """Добавить название нового репозитория"""
        name_place = self.get_element(*NewRepositoryPageLocators.NAME_NEW_REPOSITORY)
        name_place.send_keys(name_new_repository)

    @allure.step('Create repository')
    def create_repository(self):
        """Создаем репозиторий"""
        button_create_repository = WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable(NewRepositoryPageLocators.BUTTON_CREATE_REPOSITORY))
        button_create_repository.click()

    @allure.step('Check repository is create')
    def new_repository_was_created(self, name_new_repository: str):
        """Проверяем что репозиторий создан и
        мы находимся на странице созданного репозитория"""
        assert name_new_repository in self.browser.current_url, "New repository was not create"

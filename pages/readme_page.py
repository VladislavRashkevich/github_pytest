import allure
from .base_page import BasePage
from .locators import ReadmePageLocators, RepositoryPageLocators
from selenium.webdriver.support import expected_conditions as ec
from ..config import TEXT_TO_README

class ReadmePage(BasePage):

    @allure.step('Add commit title {commit_title} for readme')
    def add_commit_title_for_readme_page(self, commit_title="Create README.md"):
        commit_title_field = self.wait.until(
            ec.visibility_of_element_located(ReadmePageLocators.COMMIT_TITLE_FIELD)
        )
        commit_title_field.clear()
        commit_title_field.send_keys(commit_title)

    @allure.step('Add commit description {commit_description} for readme')
    def add_commit_description_for_readme_page(self, commit_description="Create README.md"):
        description_commit_field = self.wait.until(
            ec.visibility_of_element_located(ReadmePageLocators.COMMIT_DESCRIPTION_FIELD)
        )
        description_commit_field.clear()
        description_commit_field.send_keys(commit_description)

    @allure.step('Add information in main field readme')
    def add_information_in_readme(self):
        link_empty_readme = self.wait.until(
            ec.visibility_of_element_located(ReadmePageLocators.MAIN_README_FIELD)
        )
        link_empty_readme.clear()
        link_empty_readme.send_keys(TEXT_TO_README)

    @allure.step('Commiting file')
    def go_commit_new_file(self):
        submit_file_button = self.wait.until(
            ec.element_to_be_clickable(ReadmePageLocators.SUBMIT_FILE_BUTTON)
        )
        submit_file_button.click()

    @allure.step('Check readme in repository')
    def should_be_readme_in_list_files_in_repository(self):
        files_in_repositories = self.wait.until(
            ec.presence_of_all_elements_located(RepositoryPageLocators.FILE_IN_REPOSITORY)
        )
        lst = list(map(lambda x: x.text, files_in_repositories))

        assert "README.md" in lst, "README.md has not been added"

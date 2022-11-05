import allure
from .base_page import BasePage
from .locators import ReadmePageLocators, RepositoryPageLocators
from ..config import TEXT_TO_README


class ReadmePage(BasePage):

    locators = ReadmePageLocators
    text_to_readme = TEXT_TO_README

    @allure.step('Add commit title {commit_title} for readme')
    def add_commit_title_for_readme_page(self, commit_title="Create README.md"):
        commit_title_field = self.browser_helper.element_is_visible(self.locators.COMMIT_TITLE_FIELD)
        commit_title_field.clear()
        self.browser_helper.send_keys_in_element(commit_title_field, commit_title)

    @allure.step('Add commit description {commit_description} for readme')
    def add_commit_description_for_readme_page(self, commit_description="Create README.md"):
        description_commit_field = self.browser_helper.element_is_visible(self.locators.COMMIT_DESCRIPTION_FIELD)
        description_commit_field.clear()
        self.browser_helper.send_keys_in_element(description_commit_field, commit_description)

    @allure.step('Add information in main field readme')
    def add_information_in_readme(self):
        link_empty_readme = self.browser_helper.element_is_visible(self.locators.MAIN_README_FIELD)
        link_empty_readme.clear()
        self.browser_helper.send_keys_in_element(link_empty_readme, self.text_to_readme)

    @allure.step('Commiting file')
    def go_commit_new_file(self):
        submit_file_button = self.browser_helper.element_is_clickable(self.locators.SUBMIT_FILE_BUTTON)
        submit_file_button.click()

    @allure.step('Verification readme in repository')
    def should_be_readme_in_list_files_in_repository(self):
        files_in_repositories = self.browser_helper.elements_are_visible(RepositoryPageLocators.FILE_IN_REPOSITORY)
        lst = list(map(lambda x: x.text, files_in_repositories))

        assert "README.md" in lst, "README.md has not been added"

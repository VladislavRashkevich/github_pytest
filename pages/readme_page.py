from .base_page import BasePage
from .locators import ReadmePageLocators, RepositoryPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ReadmePage(BasePage):

    README_TITLE = "README.md"

    text_to_readme =\
        """<h1>hello Readme</h1>
    I created you with a few problems, but...
    if you here, i have a success!!!! 
    Cheers !!! 
    """
    def add_commit_title_for_readme_page(self, commit_title="Create README.md"):
        commit_title_field = WebDriverWait(self.browser, 8).until(
            ec.visibility_of_element_located(ReadmePageLocators.COMMIT_TITLE_FIELD)
        )
        commit_title_field.clear()
        commit_title_field.send_keys(commit_title)

    def add_commit_description_for_readme_page(self, commit_description="Create README.md"):
        description_commit_field = WebDriverWait(self.browser, 8).until(
            ec.visibility_of_element_located(ReadmePageLocators.COMMIT_DESCRIPTION_FIELD)
        )
        description_commit_field.clear()
        description_commit_field.send_keys(commit_description)


    def add_information_in_readme(self):
        link_empty_readme = WebDriverWait(self.browser, 8).until(
            ec.visibility_of_element_located(ReadmePageLocators.MAIN_README_FIELD)
        )
        link_empty_readme.clear()
        link_empty_readme.send_keys(ReadmePage.text_to_readme)

    def go_commit_new_file(self):
        submit_file_button = WebDriverWait(self.browser, 8).until(
            ec.element_to_be_clickable(ReadmePageLocators.SUBMIT_FILE_BUTTON )
        )
        submit_file_button.click()


    def should_be_readme_in_list_files_in_repository(self):
        files_in_repositories = WebDriverWait(self.browser, 8).until(
            ec.presence_of_all_elements_located(RepositoryPageLocators.FILE_IN_REPOSITORY)
        )
        lst = list(map(lambda x: x.text, files_in_repositories))
        assert "README.md" in lst, "README.md has not been added"



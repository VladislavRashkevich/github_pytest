import pytest
import allure
from .pages.login_page import LoginPage
from .pages.main_user_page import MainUserPage
from .pages.new_repository_page import NewRepositoryPage
from .pages.repository_page import RepositoryPage
from .pages.repository_setting_page import RepositorySettingPage
from .pages.readme_page import ReadmePage
from .config import USERNAME, PASSWORD, LOGIN_PAGE_LINK, NAME_NEW_REPOSITORY, NEW_REPO_NAME


@allure.feature("Actions with repositories")
class TestUserCanCreateRepository:

    @pytest.fixture(scope="function", autouse=True)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Sign in")
    def setup(self, browser, link=LOGIN_PAGE_LINK):
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.authentication_user(USERNAME, PASSWORD)
        self.link = browser.current_url

    @pytest.mark.create_rep
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Create new repository')
    def test_user_can_create_new_repository(self, browser, name_new_repository=NAME_NEW_REPOSITORY):
        page = MainUserPage(browser, self.link)
        page.go_to_page_for_create_new_repository()
        create_new_repository_page = NewRepositoryPage(browser, browser.current_url)
        create_new_repository_page.create_new_repository(name_new_repository)
        create_new_repository_page.new_repo_should_be_created(name_new_repository)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Rename repository')
    def test_user_can_rename_repository(self, browser, new_repo_name=NEW_REPO_NAME):
        page = MainUserPage(browser, self.link)
        page.go_to_repository_page()
        page_repository = RepositoryPage(browser, browser.current_url)
        page_repository.go_to_repository_setting()
        page_repository_setting = RepositorySettingPage(browser, browser.current_url)
        page_repository_setting.rename_repository(new_repo_name)
        page_repository_setting.should_be_rename_repository(new_repo_name)

    @pytest.mark.add_readme
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Add readme in new repository')
    def test_user_can_add_readme(self, browser):
        page = MainUserPage(browser, self.link)
        page.go_to_repository_page()
        repository_page = RepositoryPage(browser, browser.current_url)
        repository_page.go_to_new_readme_page()
        readme_page = ReadmePage(browser, browser.current_url)
        readme_page.add_information_in_readme()
        readme_page.add_commit_title_for_readme_page()
        readme_page.add_commit_description_for_readme_page()
        readme_page.go_commit_new_file()
        readme_page.should_be_readme_in_list_files_in_repository()

    @pytest.mark.delete_rep
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Delete repository')
    def test_user_can_delete_repository(self, browser):
        page = MainUserPage(browser, self.link)
        page.go_to_repository_page()
        page_repository = RepositoryPage(browser, browser.current_url)
        page_repository.go_to_repository_setting()
        page_repository_setting = RepositorySettingPage(browser, browser.current_url)
        page_repository_setting.delete_repository()
        page_repository_setting.should_be_message_repository_is_empty()


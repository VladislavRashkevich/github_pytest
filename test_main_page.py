from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.skip
def test_go_to_login_page(browser):
    link = "https://github.com"
    main_page = MainPage(browser, link)
    main_page.open()
    time.sleep(6)
    main_page.should_be_login_link()
    main_page.go_to_login_page()
    time.sleep(5)


def test_user_can_authentication_from_start_page(browser):
    link = "https://github.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    username = "VladislavTest"
    password = "SecondTestAcc123"
    login_page.authentication_user(username, password)
    login_page.should_be_authorized_user()

@pytest.mark.skip
def test_it_is_login_page(browser):
    link = "https://github.com/login"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    username = "VladislavTest"
    password = "SecondTestAcc123"
    login_page.authentication_user(username, password)
    login_page.should_be_authorized_user()

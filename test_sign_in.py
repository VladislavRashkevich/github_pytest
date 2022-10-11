from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_authentication_from_start_page(browser):
    link = "https://github.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    username = "VladislavTest"
    password = "SecondTestAcc123"
    login_page.authentication_user(username, password)
    login_page.should_be_authorized_user()

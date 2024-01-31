import allure
import os
import pytest

from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.library_page import LibraryPage
from dotenv import load_dotenv

load_dotenv()


@allure.feature("Authorization")
@allure.title("Entering valid credentials")
def test_login_using_valid_credentials(page):
    BasePage(page).open_the_page(LoginPage.page_url)
    login_page = LoginPage(page)
    login_page.login(os.getenv('NAME'), os.getenv('PASSWORD'))
    LibraryPage(page)


@allure.feature("Authorization")
@allure.title("Entering invalid Username; invalid Password; invalid Username and Password")
@pytest.mark.parametrize('username, password',
                         [('invalid_username', os.getenv('PASSWORD')),
                          (os.getenv('NAME'), 'invalid_password'),
                          ('invalid_username', 'invalid_password')])
def test_login_using_invalid_credentials(page, username, password):
    BasePage(page).open_the_page(LoginPage.page_url)
    login_page = LoginPage(page)
    login_page.login(username, password)
    login_page.check_if_the_following_text_is_present_in_the_alert_dialog('Invalid login credentials')
    login_page.check_if_the_page_title_is('Login')

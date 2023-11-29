from pages.base_page import BasePage
from pages.library_page import LibraryPage
import allure
import os


@allure.feature("Authorization")
@allure.title("Log in test")
def test_log_in(page):
    base_page = BasePage(page)
    base_page.open_base_page()
    base_page.input_login(os.getenv('NAME'))
    base_page.input_password(os.getenv('PASSWORD'))
    base_page.click_login_button()

@allure.feature("Uploading assets")
@allure.title("Upload JPG")
def test_upload_jmg(api_auth):
    library_page = LibraryPage(api_auth)
    library_page.open_library_page()
    library_page.click_upload_navigation_link()


@allure.feature("Uploading assets")
@allure.title("Upload JPG2")
def test_upload_jmg2(api_auth):
    library_page = LibraryPage(api_auth)
    library_page.open_library_page()
    library_page.click_upload_navigation_link()
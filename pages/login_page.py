from playwright.sync_api import expect
from dotenv import load_dotenv
import allure

from pages.base_page import BasePage
from pages._locators import LoginPageLocators

load_dotenv()


class LoginPage(BasePage):
    page_url = '/ams/muci'

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        if self.page.title() != 'Login':
            raise Exception(f'This is not Login Page, current Page is: {self.page.title()} ({self.page.url})')

    def login(self, username, password):
        with allure.step('Enter Username, Password and click Login button'):
            self.page.get_by_label('Username').fill(username)
            self.page.get_by_label('Password').fill(password)
            self.page.locator(LoginPageLocators.LOGIN_BUTTON).click()

    def enter_username(self, username):
        with allure.step('Enter Username'):
            self.page.get_by_label('Username').fill(username)

    def enter_password(self, password):
        with allure.step('Enter Password'):
            self.page.get_by_label('Password').fill(password)

    def click_login_button(self):
        with allure.step('Click Login button'):
            self.page.locator(LoginPageLocators.LOGIN_BUTTON).click()

    def auth_verification(self):
        with allure.step('Verification of authorization and Library page opening'):
            expect(self.page).to_have_title(' Genus Media Upshot | Library')

    def check_if_the_following_text_is_present_in_the_alert_dialog(self, alert_dialog_message_text):
        with allure.step('Verification of the alert dialog message text'):
            self.page.on('dialog', lambda dialog: dialog.accept())
            with self.page.expect_event('dialog') as dialog_info:
                self.page.get_by_role('dialog')
            dialog_value = dialog_info.value
            assert dialog_value.message == alert_dialog_message_text

    def check_if_the_page_title_is(self, title):
        with allure.step('Verification of the page title'):
            expect(self.page).to_have_title(title)

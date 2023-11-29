import os
import requests
import base64
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
from pathlib import Path
import allure


load_dotenv()

login_button = "//button[text()='Login']"


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_base_page(self):
        with allure.step('Open Base Page'):
            self.page.goto(os.getenv('BASEURL'))

    def input_login(self, username):
        with allure.step('Enter Username'):
            self.page.get_by_label('Username').fill(username)

    def input_password(self, password):
        with allure.step('Enter Password'):
            self.page.get_by_label('Password').fill(password)

    def click_login_button(self):
        with allure.step('Click Login button'):
            self.page.locator(login_button).click()

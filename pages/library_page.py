import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages._locators import LibraryPageLocators


class LibraryPage(BasePage):
    page_url = '/ams/muci/library'

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        if self.page.title() != 'Genus Media Upshot | Library':
            raise Exception(f'This is not the Library Page, current Page is: {self.page.title()} ({self.page.url})')

    def get_recently_uploaded_asset_by_doc_title(self, document_title):
        with allure.step('Get last uploaded asset from recently uploaded carousel'):
            return self.page.locator(LibraryPageLocators.get_recently_uploaded_asset_locator_by_(document_title)).first

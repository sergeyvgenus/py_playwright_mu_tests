import allure
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages._locators import UploadPageLocators

load_dotenv()


class UploadPage(BasePage):
    page_url = '/ams/muci/upload'

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        if self.page.title() != 'Genus Media Upshot | Upload':
            raise Exception(f'This is not the Upload Page, current Page is: {self.page.title()} ({self.page.url})')

    def click_rich_media(self):
        with allure.step('Select RichMedia item type'):
            self.page.locator(UploadPageLocators.RICH_MEDIA_TYPE).click()

    def select_dublin_core_type(self):
        with allure.step('Select DublinCore item type'):
            self.page.locator(UploadPageLocators.DUBLIN_CORE_TYPE).click()

    def click_assign_metadata(self):
        with allure.step('Click Assign Metadata panel'):
            self.page.locator(UploadPageLocators.ASSIGN_METADATA_PANE).click()

    def input_document_title(self, doctitle):
        with allure.step('Enter Document Title'):
            self.page.locator(UploadPageLocators.DOCUMENT_TITLE_FIELD).fill(doctitle)

    def select_file_to_upload(self, file_path):
        with allure.step('Click Select Files button and enter the path to the file'):
            try:
                self.page.set_input_files(UploadPageLocators.SELECT_FILES_BUTTON, file_path)
            except FileNotFoundError as err:
                exit(f'Check if the file name and path are correct. {err}')

    def click_start_button(self):
        with allure.step('Click Star button'):
            self.page.locator(UploadPageLocators.START_BUTTON).click()

    def waiting_for_upload(self):
        with allure.step('Wait for the file upload to complete successfully'):
            progress = self.page.locator(UploadPageLocators.PROGRESS_STATUS)
            expect(progress).to_have_js_property("textContent", "Complete", timeout=90_000)

    def click_uploaded_file_link(self, filename):
        with allure.step('Click uploaded file link'):
            self.page.get_by_text(filename).click()

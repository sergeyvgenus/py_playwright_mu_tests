import allure
from dotenv import load_dotenv
import os
from playwright.sync_api import Page

from pages._locators import BasePageLocators

load_dotenv()


class BasePage:
    base_url = os.getenv('BASEURL')
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_the_page(self, page_url):
        with allure.step(f'Open Test Page: {os.getenv("BASEURL")}{page_url}'):
            self.page.goto(f'{os.getenv("BASEURL")}{page_url}')

    # def open_the_page(self):
    #     with allure.step('Open the Page'):
    #         if self.page_url:
    #             self.page.goto(f'{self.base_url}{self.page_url}'
    #         else:
    #             raise Exception('Check the page_url variable')

    def click_upload_navigation_link(self):
        with allure.step('Click Upload navigation link'):
            self.page.locator(BasePageLocators.UPLOAD_NAVIGATION_LINK).click()

    def click_library_navigation_link(self):
        with allure.step('Click Library navigation link'):
            self.page.locator(BasePageLocators.LIBRARY_NAVIGATION_LINK).click()

    # def delete_the_uploaded_asset(self):
    #     with allure.step('Delete the uploaded asset'):
    #         asset = self.page.locator(BasePageLocators.UPLOADED_FILE_ASSET_LINK).first
    #         asset_id = asset.get_attribute('dnddata')
    #         os.environ['ASSETID'] = asset_id
    #         userpass = os.getenv('NAME') + ':' + os.getenv('PASSWORD')
    #         encodedusepass = base64.b64encode(userpass.encode()).decode()
    #         delete_asset_request = self.page.request.delete(
    #             os.getenv('RESTURL') + os.getenv('ASSETID'),
    #             headers={
    #                 "Accept": "*/*",
    #                 "Authorization": "Basic: %s" % encodedusepass
    #             }
    #         )
    #         assert delete_asset_request.ok

    @staticmethod
    def get_asset_id(asset):
        with allure.step('Get the asset ID'):
            return asset.get_attribute('dnddata')

    @staticmethod
    def delete_asset_by_id_via_api(get_asset_id, api_request_context):
        with allure.step('Delete asset by its ID via API'):
            delete_asset_api_response = api_request_context.delete(f'{os.getenv("RESTURL")}{get_asset_id}')
            if not delete_asset_api_response.ok:
                raise Exception

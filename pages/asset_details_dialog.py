import allure
from playwright.sync_api import Page, expect

from pages._locators import AssetDetailsDialogLocators
from pages.base_page import BasePage


class AssetDetailsDialog(BasePage):
    page_url = None

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.suggested_name = None

    def check_if_the_ingest_tab_is_open(self):
        with allure.step('Check if the Ingest tab is open'):
            expect(self.page.locator(AssetDetailsDialogLocators.INGEST_TAB)).to_have_attribute('aria-selected', 'true')
            expect(self.page.locator(AssetDetailsDialogLocators.ASSET_STATUS_SECTION))

    def check_if_preview_is_presented(self):
        with allure.step('Check if Preview is presented'):
            expect(self.page.locator(AssetDetailsDialogLocators.PREVIEW))

    def check_if_mu_player_controlbar_is_presented(self):
        with allure.step('Check if MU Player (Document Viewer) is presented and available'):
            expect(self.page.locator(AssetDetailsDialogLocators.MU_PLAYER_CONTROLBAR))

    def click_parts_tab(self):
        with allure.step('Click Parts tab'):
            self.page.locator(AssetDetailsDialogLocators.PARTS_TAB).click()

    def check_if_the_link_to_download_the_original_part_is_presented(self):
        with allure.step('Check if the link to Download the Original part is presented'):
            expect(self.page.locator(AssetDetailsDialogLocators.ORIGINAL_PART_DOWNLOAD_LINK))

    def click_download_the_original_part_link(self):
        with allure.step('Click Download the Original part link'):
            with self.page.expect_download() as download_info:
                # Perform the action that initiates download
                self.page.locator(AssetDetailsDialogLocators.ORIGINAL_PART_DOWNLOAD_LINK).click()
            download = download_info.value
            self.suggested_name = download.suggested_filename
            download.cancel()

    def check_if_the_suggested_name_of_the_original_part_is_(self, filename):
        with allure.step('Check if the suggested name of the original part is correct'):
            assert self.suggested_name == filename

    def close_asset_details_window(self):
        with allure.step('Close Asset Details window'):
            self.page.locator(AssetDetailsDialogLocators.CLOSE_X_ICON).click()

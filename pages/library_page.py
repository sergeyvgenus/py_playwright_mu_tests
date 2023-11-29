import os
import requests
import base64
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
import allure


load_dotenv()

library_navigation_link = "a[href='../library']"
upload_navigation_link = "//a[text()='Upload']"
rich_media_type = "//span[text()='RichMedia']"
dublin_core_type = "//td[text()='DublinCore']"
select_files_button = "//input[@name='uploadedfiles[]']"
assign_metadata_pane = "//span[text()='Assign Metadata']"
document_title_field = "//input[@id='_MetadataEditor_control_6']"
start_button = "//span[text()='Start']"
progress_status = "//td[@class='uploaderFileList-progress']"
# uploaded_file_link = "//a[text()='upload_img.jpg']"
ingest_tab = "//span[text()='Ingest']"
parts_tab = "(//div[contains(.,'Parts')])[11]"
asset_status_section = "//h2[text()='Asset status, security, and binaries'])"
original_part_download_link = "//table[@class='itemsTable itemsTable-typeImage']/tr/td[contains(text(), 'Original')]/parent::tr//a"
close_x_icon = "(//span[contains(.,'x')])[8]"
uploaded_file_asset_link = "//*[text() = 'upload_img']//..//..//..//.."


class LibraryPage:
    def __init__(self, page: Page):
        self.suggested_name = None
        self.page = page

    def open_library_page(self):
        with allure.step('Open Library Page'):
            self.page.goto(os.getenv('BASEURL')+'/library/')

    def click_upload_navigation_link(self):
        with allure.step('Click Upload navigation link'):
            self.page.locator(upload_navigation_link).click()

    def click_rich_media(self):
        with allure.step('Select RichMedia item type'):
            self.page.locator(rich_media_type).click()

    def select_dublin_core_type(self):
        with allure.step('Select DublinCore item type'):
            self.page.locator(dublin_core_type).click()

    def click_assign_metadata(self):
        with allure.step('Click Assign Metadata panel'):
            self.page.locator(assign_metadata_pane).click()

    def input_document_title(self, doctitle):
        with allure.step('Enter Document Title'):
            self.page.locator(document_title_field).fill(doctitle)

    def select_file_to_upload(self, file_path):
        with allure.step('Click Select Files button and enter the path to the file'):
            # cwd = os.getcwd()
            # file_path = os.path.join(cwd, 'testdata\\upload_img.jpg')
            # file_path = 'C:\\Projects\\GIT\\MU\\PyAutoTests\\py_playwright_mu_tests\\testdata\\upload_img.jpg'
            self.page.set_input_files(select_files_button, file_path)

    def click_start_button(self):
        with allure.step('Click Star button'):
            self.page.locator(start_button).click()

    def waiting_for_upload(self):
        with allure.step('Wait for the file upload to complete successfully'):
            progress = self.page.locator(progress_status)
            expect(progress).to_have_js_property("textContent", "Complete", timeout=90_000)

    def click_uploaded_file_link(self, filename):
        with allure.step('Click uploaded file link'):
            self.page.get_by_text(filename).click()

    def check_if_the_ingest_tab_is_open(self):
        with allure.step('Check if the Ingest tab is open'):
            expect(self.page.locator(ingest_tab)).to_have_attribute('aria-selected', 'true')
            expect(self.page.locator(asset_status_section))

    def click_parts_tab(self):
        with allure.step('Click Parts tab'):
            self.page.locator(parts_tab).click()

    def check_if_the_link_to_download_the_original_part_is_presented(self):
        with allure.step('Check if the link to Download the Original part is presented'):
            expect(self.page.locator(original_part_download_link))

    def click_download_the_original_part_link(self):
        with allure.step('Click Download the Original part link'):
            with self.page.expect_download() as download_info:
                # Perform the action that initiates download
                self.page.locator(original_part_download_link).click()
            download = download_info.value
            self.suggested_name = download.suggested_filename
            download.cancel()

    def check_if_the_suggested_name_is_correct(self, filename):
        with allure.step('Check if the suggested name is correct'):
            assert self.suggested_name == filename

    def close_asset_details_window(self):
        with allure.step('Close Asset Details window'):
            self.page.locator(close_x_icon).click()

    def click_library_navigation_link(self):
        with allure.step('Click Library navigation link'):
            self.page.locator(library_navigation_link).click()

    def delete_the_uploaded_asset(self):
        with allure.step('Delete the uploaded asset'):
            asset = self.page.locator(uploaded_file_asset_link).first
            asset_id = asset.get_attribute('dnddata')
            os.environ['ASSETID'] = asset_id
            userpass = os.getenv('NAME') + ':' + os.getenv('PASSWORD')
            encodedusepass = base64.b64encode(userpass.encode()).decode()
            delasset = self.page.request.delete(
                os.getenv('RESTURL') + os.getenv('ASSETID'),
                headers={
                    "Accept": "*/*",
                    "Authorization": "Basic: %s" % encodedusepass
                }
            )
            assert delasset.ok

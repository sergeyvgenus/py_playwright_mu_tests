import allure

from pages.asset_details_dialog import AssetDetailsDialog
from pages.base_page import BasePage
from pages.library_page import LibraryPage
from pages.upload_page import UploadPage


@allure.feature("Uploading assets")
@allure.title("Upload JPG")
def test_upload_jmg(api_auth, api_request_context):
    page = BasePage(api_auth)
    page.open_the_page(LibraryPage.page_url)
    library_page = LibraryPage(api_auth)
    library_page.click_upload_navigation_link()
    upload_page = UploadPage(api_auth)
    upload_page.click_rich_media()
    upload_page.select_dublin_core_type()
    upload_page.click_assign_metadata()
    upload_page.input_document_title('upload_img')
    upload_page.select_file_to_upload('tests/testdata/upload_img.jpg')
    upload_page.click_start_button()
    upload_page.waiting_for_upload()
    upload_page.click_uploaded_file_link('upload_img.jpg')
    asset_details_dialog = AssetDetailsDialog(api_auth)
    asset_details_dialog.check_if_the_ingest_tab_is_open()
    asset_details_dialog.click_parts_tab()
    # asset_details_dialog.check_if_the_link_to_download_the_original_part_is_presented()
    asset_details_dialog.click_download_the_original_part_link()
    asset_details_dialog.check_if_the_suggested_name_of_the_original_part_is_('upload_img.jpg')
    asset_details_dialog.close_asset_details_window()
    upload_page.click_library_navigation_link()
    library_page.delete_asset_by_id_via_api(
        library_page.get_asset_id(
            library_page.get_recently_uploaded_asset_by_doc_title('upload_img')),
        api_request_context)


@allure.feature("Uploading assets")
@allure.title("Upload PDF")
def test_upload_jmg2(api_auth, api_request_context):
    page = BasePage(api_auth)
    page.open_the_page(UploadPage.page_url)
    upload_page = UploadPage(api_auth)
    upload_page.click_rich_media()
    upload_page.select_dublin_core_type()
    upload_page.click_assign_metadata()
    upload_page.input_document_title('upload_pdf')
    upload_page.select_file_to_upload('tests/testdata/upload_pdf.pdf')
    upload_page.click_start_button()
    upload_page.waiting_for_upload()
    upload_page.click_uploaded_file_link('upload_pdf.pdf')
    asset_details_dialog = AssetDetailsDialog(api_auth)
    asset_details_dialog.check_if_the_ingest_tab_is_open()
    asset_details_dialog.check_if_preview_is_presented()
    asset_details_dialog.check_if_mu_player_controlbar_is_presented()
    asset_details_dialog.click_parts_tab()
    asset_details_dialog.click_download_the_original_part_link()
    asset_details_dialog.check_if_the_suggested_name_of_the_original_part_is_('upload_pdf.pdf')
    asset_details_dialog.close_asset_details_window()
    upload_page.click_library_navigation_link()
    library_page = LibraryPage(api_auth)
    library_page.delete_asset_by_id_via_api(
        library_page.get_asset_id(
            library_page.get_recently_uploaded_asset_by_doc_title('upload_pdf')),
        api_request_context)

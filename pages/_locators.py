class BasePageLocators:
    LIBRARY_NAVIGATION_LINK = "a[href='../library']"
    UPLOAD_NAVIGATION_LINK = "//a[text()='Upload']"
    UPLOADED_FILE_ASSET_LINK = "//*[text() = 'upload_img']//..//..//..//.."


class LoginPageLocators:
    LOGIN_BUTTON = "//button[text()='Login']"


class LibraryPageLocators:
    @staticmethod
    def get_recently_uploaded_asset_locator_by_(document_title):
        return f'//*[text() = "{document_title}"]//..//..//..//..'


class UploadPageLocators:
    RICH_MEDIA_TYPE = "//span[text()='RichMedia']"
    DUBLIN_CORE_TYPE = "//td[text()='DublinCore']"
    SELECT_FILES_BUTTON = "//input[@name='uploadedfiles[]']"
    ASSIGN_METADATA_PANE = "//span[text()='Assign Metadata']"
    DOCUMENT_TITLE_FIELD = "//input[@id='_MetadataEditor_control_6']"
    START_BUTTON = "//span[text()='Start']"
    PROGRESS_STATUS = "//td[@class='uploaderFileList-progress']"


class AssetDetailsDialogLocators:
    INGEST_TAB = "//span[text()='Ingest']"
    PARTS_TAB = "(//div[contains(.,'Parts')])[11]"
    ASSET_STATUS_SECTION = "//h2[text()='Asset status, security, and binaries'])"
    ORIGINAL_PART_DOWNLOAD_LINK = \
        "//table[contains(@class, 'itemsTable itemsTable')][1]/tr/td[contains(text(), 'Original')]/parent::tr//a"
    CLOSE_X_ICON = "(//span[contains(.,'x')])[8]"
    PREVIEW = "//@src[contains(.,'Preview1')]"
    MU_PLAYER_CONTROLBAR = "mu-player-controlbar"

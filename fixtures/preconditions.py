import base64
import pytest
import os
import allure
from dotenv import load_dotenv
from playwright.sync_api import Playwright, Browser

load_dotenv()


@pytest.fixture(scope="session")
@allure.title("Context_generation: base_url authorization")
def api_auth(playwright: Playwright, browser: Browser):
    userpass = os.getenv('NAME') + ':' + os.getenv('PASSWORD')
    encodedusepass = base64.b64encode(userpass.encode()).decode()
    request_context = playwright.request.new_context(
        base_url="http://qa-mu70tomcat.genus.qa",
        extra_http_headers={'Authorization': "Basic " + encodedusepass}
    )
    request_context.get('http://qa-mu70tomcat.genus.qa/ams/muci')
    state = request_context.storage_state()
    context = browser.new_context(storage_state=state)
    return context.new_page()

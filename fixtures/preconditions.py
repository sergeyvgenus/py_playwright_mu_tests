import allure
import base64
from dotenv import load_dotenv
import os
import pytest
from playwright.sync_api import Playwright, Browser, APIRequestContext
from typing import Generator

load_dotenv()


@pytest.fixture(scope="session")
@allure.title("Context generation: page with authenticated state")
def api_auth(playwright: Playwright, browser: Browser):
    userpass = os.getenv('NAME') + ':' + os.getenv('PASSWORD')
    encodedusepass = base64.b64encode(userpass.encode()).decode()
    request_context = playwright.request.new_context(
        base_url=os.getenv('BASEURL'),
        extra_http_headers={'Authorization': "Basic " + encodedusepass}
    )
    try:
        request_context.get(f'{os.getenv("BASEURL")}{os.getenv("MUCI_URL_PART")}')
        state = request_context.storage_state()
        context = browser.new_context(storage_state=state)
        return context.new_page()
    except Exception as err:
        print('Check connection to server or VPN.', err)



@pytest.fixture(scope="session")
@allure.title("Context generation: authenticated state")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    userpass = os.getenv('NAME') + ':' + os.getenv('PASSWORD')
    encodedusepass = base64.b64encode(userpass.encode()).decode()
    request_context = playwright.request.new_context(
        base_url=os.getenv('BASEURL'),
        extra_http_headers={'Authorization': "Basic " + encodedusepass}
    )
    try:
        request_context.get(os.getenv('BASEURL'))
    except Exception as err:
        print("Check connection to server or VPN.", err)
    yield request_context
    request_context.dispose()
    
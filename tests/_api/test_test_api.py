import os
import allure
from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext
from dotenv import load_dotenv
import base64
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


load_dotenv()


@pytest.fixture(scope="session")
@allure.title("Context_generation: base_url authorization")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    userpass = os.getenv('NAME') + ':' + os.getenv('PASSWORD')
    encodedusepass = base64.b64encode(userpass.encode()).decode()
    request_context = playwright.request.new_context(
        base_url="http://qa-mu70tomcat.genus.qa",
        extra_http_headers={'Authorization': "Basic " + encodedusepass}
    )
    yield request_context
    request_context.dispose()


@allure.feature("Item Type")
@allure.story("Get Item Type")
@allure.title("Get Item Type Test")
def test_get_item_types(api_request_context: APIRequestContext):
    response = api_request_context.get(f"{os.getenv('APIBASEURL')}/ams/rest/item-types")
    if response.status != 200:
        raise ValueError(f"Request test_get_item_types failed {response.status}")
    response_content = response.text()
    root = ET.fromstring(response_content)
    # print(root)
    # print(root.tag, root.attrib)
    print([child.attrib["name"] for child in root])
    assert [child.attrib["name"] for child in root] == ['RichMedia', 'AMS_COLLECTION', 'DublinCore', 'CalendarEvents']
    soup = BeautifulSoup(response_content, "lxml-xml")
    print(soup.prettify())
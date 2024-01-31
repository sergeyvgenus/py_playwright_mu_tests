import os
import allure
from playwright.sync_api import APIRequestContext
from dotenv import load_dotenv
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

load_dotenv()


@allure.feature("Item Type")
@allure.story("Get Item Type")
@allure.title("Get Item Type Test")
def test_get_item_types(api_request_context: APIRequestContext):
    response = api_request_context.get(f"{os.getenv('APIBASEURL')}/ams/rest/item-types")
    if response.status != 200:
        raise ValueError(f"Request test_get_item_types failed {response.status}")
    response_content = response.text()
    root = ET.fromstring(response_content)
    print([child.attrib["name"] for child in root])
    assert ([child.attrib["name"] for child in root] ==
            ['RichMedia', 'AMS_COLLECTION', 'DublinCore', 'CalendarEvents'])
    soup = BeautifulSoup(response_content, "lxml-xml")
    print(soup.prettify())


@allure.feature("Item Type")
@allure.story("Get Item Type")
@allure.title("Get Item Type Test 2")
def test_get_item_types_2(api_request_context: APIRequestContext):
    response = api_request_context.get(f"{os.getenv('APIBASEURL')}/ams/rest/item-types")
    if response.status != 200:
        raise ValueError(f"Request test_get_item_types failed {response.status}")
    response_content = response.text()
    root = ET.fromstring(response_content)
    print([child.attrib["name"] for child in root])
    assert ([child.attrib["name"] for child in root] ==
            ['RichMedia', 'AMS_COLLECTION', 'DublinCore', 'CalendarEvents'])
    soup = BeautifulSoup(response_content, "lxml-xml")
    print(soup.prettify())

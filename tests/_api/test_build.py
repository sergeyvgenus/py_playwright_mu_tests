import os
import allure
from playwright.sync_api import APIRequestContext
from dotenv import load_dotenv

load_dotenv()


@allure.feature("Build Info")
@allure.story("Get Build Info")
@allure.title("Get Build Info Test")
def test_get_build_info(api_request_context: APIRequestContext):
    response = api_request_context.get('/mediaupshot/services/contentEngine/json/hierarchy/public')
    print(response.headers)
    if response.status != 200:
        raise ValueError(f"Request test_get_build_info failed {response.status}")
    response_json_content = response.json()
    print(response.status)
    print(response_json_content)
    print(type(response_json_content['collection']))
    for collection in response_json_content['collection']:
        print(collection['name'])

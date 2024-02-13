import os
import allure
from playwright.sync_api import APIRequestContext
from dotenv import load_dotenv

load_dotenv()


@allure.feature("Collections")
@allure.story("Get Public Collections Hierarchy")
@allure.title("Get Public Collections Hierarchy Test")
def test_get_public_collections_hierarchy(api_request_context: APIRequestContext):
    response = api_request_context.get('/mediaupshot/services/contentEngine/json/hierarchy/public')
    print(response.headers)
    if response.status != 200:
        raise ValueError(f"Request test_get_build_info failed {response.status}")
    response_json_content = response.json()
    print(response.status)
    print(response_json_content)
    print(type(response_json_content['collection']))
    dict = [collection['name'] for collection in response_json_content['collection']]
    print(dict)
    assert 'MU+Smoke+Test' in dict
 

@allure.feature("Build Info")
@allure.story("Get Build Info")
@allure.title("Get Build Info Test")
def test_get_build_info(api_request_context: APIRequestContext):
    response = api_request_context.get('/mediaupshot/services/contentEngine/json/build-info')
    print(response.headers)
    if response.status != 200:
        raise ValueError(f"Request test_get_build_info failed {response.status}")
    response_json_content = response.json()
    print(response.status)
    print(response_json_content)
    print(f"{response_json_content['product-name']} version:{response_json_content['product-version']}")
    assert response_json_content['product-version'] == '7.1.0.6'

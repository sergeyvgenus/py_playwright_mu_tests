import pytest
from playwright.sync_api import Page, expect
import logging
import pytest_html
import allure


@pytest.mark.skip
def test_for_githab(page: Page):
    # page.context.tracing.start(screenshots=True, snapshots=True)
    page.goto('https://pumapro.ru/', timeout=90000)
    page.get_by_text('посмотреть предложение для вузов')

    # page.wait_for_timeout(3000)
    # page.once("load", lambda: print("page loaded!"))
    # print("Hello")
    page.screenshot(
        path="tests/screenshots/puma_pro.jpg",
    )
    # page.context.tracing.stop(path="trace.zip")
# test

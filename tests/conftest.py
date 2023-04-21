import pytest
from playwright.sync_api import Page
from playwright.sync_api import BrowserType
from typing import Dict


# @pytest.fixture(scope="session")
# def context(
#     browser_type: BrowserType,
#     browser_type_launch_args: Dict,
#     browser_context_args: {
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         },
#         "ignore_https_errors": True
#     }
# ):
#     context = browser_type.launch_persistent_context("./foobar", **{
#         **browser_type_launch_args,
#         **browser_context_args,
#         "locale": "de-DE",
#     })
#     yield context
#     context.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    print()
    print("ZZZZZZZZZZZZZZZZZ  Before All ZZZZZZZZZZZZZZZZZ")
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }
    print()
    print("ZZZZZZZZZZZZZZZZZ  After All ZZZZZZZZZZZZZZZZZ")


@pytest.fixture(scope="function", autouse=True)
def login_logout(page: Page, request):
    base_url = request.config.getoption("--base-url")
    page.goto("/")
    print("ZZZZZZZZZZZZZZZZZ  Before Each ZZZZZZZZZZZZZZZZZ")
    yield page
    print("ZZZZZZZZZZZZZZZZZ  After Each ZZZZZZZZZZZZZZZZZ")
    page.close()

# @pytest.fixture(scope="module", autouse=True)
# def login_logout(page: Page):
#     print("beforeAll")
#     yield page
#     print("afterAll")

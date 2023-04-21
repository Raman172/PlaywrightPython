import pytest
from playwright.sync_api import expect, BrowserContext

from page_objects.login_page import LoginPage
from page_objects.logout_page import LogoutPage


class TestLoginPage:
    # @pytest.mark.skip_browser("firefox")
    # @pytest.mark.only_browser("chromium")
    @pytest.mark.sanity
    @pytest.mark.parametrize("username, password", [("problem_user", "secret_sauce"),
                                                    ("standard_user", "secret_sauce")])
    def test_login(self, login_logout, request, username, password):
        page = login_logout
        base_url = request.config.getoption("--base-url")
        context: BrowserContext = page.context
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        login_page = LoginPage(page)
        login_page.login(username, password)
        logout_page = LogoutPage(page)
        expect(logout_page.hamburger_close).to_be_visible()
        context.tracing.stop(path="./trace1.zip")
        logout_page.logout()
        context.close()

    # @pytest.mark.skip_browser("firefox")
    # @pytest.mark.only_browser("chromium")
    @pytest.mark.skip(reason="Invalid Users Credentials Not Available")
    @pytest.mark.parametrize("username, password", [("problem_user", "secret_sauce1")])
    def test_login_error(self, login_logout, request, username, password):
        page = login_logout
        base_url = request.config.getoption("--base-url")
        context: BrowserContext = page.context
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        login_page = LoginPage(page)
        login_page.login(username, password)
        logout_page = LogoutPage(page)
        expect(logout_page.hamburger_close).to_be_visible()
        context.tracing.stop(path="./trace1.zip")
        logout_page.logout()
        context.close()

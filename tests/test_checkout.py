import pytest
from playwright.sync_api import expect, BrowserContext

from page_objects.complete_page import CompletePage
from page_objects.login_page import LoginPage
from page_objects.logout_page import LogoutPage
from page_objects.overview_page import OverviewPage
from page_objects.product_list_page import ProductListPage
from page_objects.yourcart_page import YourCartPage
from page_objects.yourinformation_page import YourInformationPage


# @pytest.mark.skip_browser("firefox")
# @pytest.mark.only_browser("chromium")
@pytest.mark.regression
def test_checkout(login_logout, request):
    page = login_logout
    base_url = request.config.getoption("--base-url")
    print("ZZZZZZZZZZZZZZZZZ  Base URL ZZZZZZZZZZZZZZZZZ")
    print(base_url)
    print("ZZZZZZZZZZZZZZZZZ  Browser ZZZZZZZZZZZZZZZZZ")
    print(request.config.getoption("--browser"))
    context: BrowserContext = page.context
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    logout_page = LogoutPage(page)
    expect(logout_page.hamburger_close).to_be_visible()
    context.tracing.stop(path="./trace2.zip")
    product_list_page = ProductListPage(page)
    product_list_page.add_to_cart()
    product_list_page.navigate_to_cart_page()
    your_cart_page = YourCartPage(page)
    your_cart_page.checkout()
    your_information_page = YourInformationPage(page)
    your_information_page.fill_user_information("FirstName", "LastName", "111011")
    overview_page = OverviewPage(page)
    overview_page.finish()
    complete_page = CompletePage(page)
    expect(complete_page.thank_you_text).to_be_visible()
    complete_page.back_home()
    logout_page.logout()
    context.close()


@pytest.mark.xfail(reason="Failing due to invalid credential")
@pytest.mark.skip(reason="Invalid Users Credentials Not Available")
# @pytest.mark.only_browser("chromium")
@pytest.mark.regression
def test_checkout_login_fail(login_logout, request):
    page = login_logout
    base_url = request.config.getoption("--base-url")
    context: BrowserContext = page.context
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    login_page = LoginPage(page)
    login_page.login("standard_user", "invalid password")
    logout_page = LogoutPage(page)
    expect(logout_page.hamburger_close).to_be_visible()
    context.close()

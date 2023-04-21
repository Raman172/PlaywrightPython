class LogoutPage:
    def __init__(self, page):
        self.page = page
        self.hamburger_close = page.locator("button[id=react-burger-menu-btn]")
        self.hamburger_open = page.get_by_role("button", name="Open Menu")
        self.logout_btn = page.get_by_role("link", name="Logout")

    def navigate(self):
        self.page.goto("/")

    def logout(self):
        self.hamburger_open.click()
        self.logout_btn.click()

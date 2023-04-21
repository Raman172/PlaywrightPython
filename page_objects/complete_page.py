class CompletePage:
    def __init__(self, page):
        self.page = page
        self.thank_you_text = page.get_by_role("heading", name="Thank you for your order!")
        self.back_home_btn = page.locator("[data-test=\"back-to-products\"]")

    def navigate(self):
        self.page.goto("/checkout-complete.html")

    def back_home(self):
        self.back_home_btn.click()


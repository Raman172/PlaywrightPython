class YourCartPage:
    def __init__(self, page):
        self.page = page
        self.product1_price_text = page.get_by_text("$")

        self.checkout_btn = page.locator("[data-test=\"checkout\"]")

    def navigate(self):
        self.page.goto("/cart.html")

    def checkout(self):
        self.checkout_btn.click()


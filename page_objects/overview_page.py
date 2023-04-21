class OverviewPage:
    def __init__(self, page):
        self.page = page
        self.finish_btn = page.locator("[data-test=\"finish\"]")

    def navigate(self):
        self.page.goto("/checkout-step-two.html")

    def finish(self):
        self.finish_btn.click()


class YourInformationPage:
    def __init__(self, page):
        self.page = page
        self.first_name_inp = page.locator("[data-test=\"firstName\"]")
        self.last_name_inp = page.locator("[data-test=\"lastName\"]")
        self.postal_code_inp = page.locator("[data-test=\"postalCode\"]")
        self.continue_btn = page.locator("[data-test=\"continue\"]")

    def navigate(self):
        self.page.goto("/checkout-step-one.html")

    def fill_user_information(self,firstname,lastname,zipcode):
        self.first_name_inp.fill(firstname)
        self.last_name_inp.fill(lastname)
        self.postal_code_inp.fill(zipcode)
        self.continue_btn.click()



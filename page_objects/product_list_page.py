class ProductListPage:
    def __init__(self, page):
        self.page = page
        self.product1_title_text = page.locator("#item_4_title_link")
        self.product1_description_text = page.get_by_text("carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromis")
        self.product1_addtocart_btn = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")

        self.cart_icon = page.locator("a").filter(has_text="1")

    def navigate(self):
        self.page.goto("/inventory.html")

    def add_to_cart(self):
        self.product1_addtocart_btn.click()

    def navigate_to_cart_page(self):
        self.cart_icon.click()

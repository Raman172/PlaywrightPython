class LoginPage:
    def __init__(self, page):
        self.page = page
        self.user_name_inp = page.locator("//input[@type='text']")
        self.user_password_inp = page.locator("//input[@type='password']")
        self.user_login_btn = page.locator("text=LOGIN")

    def navigate(self):
        self.page.goto("/")

    def login(self, user, password):
        self.user_name_inp.fill(user)
        self.user_password_inp.fill(password)
        self.user_login_btn.click()

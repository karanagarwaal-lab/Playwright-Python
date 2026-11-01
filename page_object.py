import re
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = (self.page) = self.page.title()

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username: str, password: str):
        self.page.get_by_placeholder("Enter Username").fill("Admin")
        self.page.get_by_placeholder("Enter Password").fill("admin123")

        self.page.get_by_role("button", name="Login").click()




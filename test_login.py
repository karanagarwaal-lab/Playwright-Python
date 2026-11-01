
from playwright.sync_api import Page, expect

def test_login(page: Page):

    # Step 1: Open login page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index") 
    
    page.wait_for_timeout(10000)
    
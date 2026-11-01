
from ast import Add

from playwright.sync_api import Page, expect

def test_login(page: Page):

    # Step 1: Open login page
    page.goto("https://www.orangehealth.in")

    page.wait_for_timeout(5000)

    page.locator("//span[@class='oui-typography oui-typography--transform-none oui-typography--size-18 oui-typography--weight-600 oui-typography--line-height-22 oui-typography--decoration-none oui-text-ink-900'][normalize-space()='Tests']").click()
    page.wait_for_timeout(5000)

    Blood1 = page.locator('.sku-card-title-text').filter(has_text="Vitamin B12")
    Blood1.get_by_role('button', name='+ Add').click()   
    Blood2 = page.locator('.sku-card-title-text').filter(has_text="Vitamin D, Total")
    Blood2.get_by_role('button', name='+ Add').click()
    Blood3 = page.locator('.sku-card-title-text').filter(has_text="Ferritin")
    Blood3.get_by_role('button', name='+ Add').click()

    page.wait_for_timeout(5000)
    page.locator("//button[@aria-label='Cart, 0 items']").click()
    page.locator("//span[@class='oui-typography oui-typography--transform-none oui-typography--size-14 oui-typography--weight-500 oui-typography--line-height-18 oui-typography--decoration-none oui-text-ink-white']").click()

    expect(page).to_have_title("Who is getting tested?")
    page.wait_for_timeout(5000)
    #  python -m pytest test_login_orange_test.py --headed
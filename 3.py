import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,browser= "edge")
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/") 
    page.locator("#kw").fill("what")
    page.locator("#kw").press("Enter")
    page.locator("#content_left").click()
    print(page.title())

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("lala")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("lalala")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_text("Mark all as complete").click()
    page.get_by_label("Mark all as complete").click()
    page.get_by_label("Mark all as complete").click()
    page.get_by_role("button", name="Clear completed").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

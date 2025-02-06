import pytest
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    # запуск браузера и создание в нем контекста:
    browser = playwright.chromium.launch(headless=False)  # запуск chrome (headless=False/True)
    context = browser.new_context()  # создает изолированный сеанс браузера
    page = context.new_page()  # открывает новую страницу(tab) в браузере
    # steps on page:
    page.goto("https://demo.playwright.dev/todomvc/#/")  # открыть веб-сайт
    placeholder = page.get_by_placeholder("What needs to be done?")  # находит в DOM дереве веб-элемент
    placeholder.click()
    placeholder.fill("add my first todo")
    placeholder.press("Enter")
    page.get_by_test_id("todo-title").click()
    page.get_by_label("Toggle Todo").check()

    # ---------------------
    context.close()
    browser.close()

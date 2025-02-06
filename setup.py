# first steps:
# pip install playwright
# pip install pytest
# pip install pytest-playwright

# codegen [params] [url]:
# playwright codegen demo.playwright.dev/todomvc/#/
# params:
# playwright codegen --help
# playwright codegen --viewport-size=1920,1080 https://demo.playwright.dev/todomvc/#/
# playwright codegen -o main.py https://demo.playwright.dev/todomvc/#/

# pytest params:
# pytest --headed
# pytest --browser webkit --browser firefox
# pytest --browser-channel=msedge --headed
# pytest --slowmo 3000
# pytest --device="iPhone 13 Mini"  all devices:
# https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json
# pytest --output test-results ??
# pytest --tracing=on ??
# pytest --video=on
# pytest --screenshot=on/only-on-failure
# pytest --full-page-screenshot=on/only-on-failure


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

# run without pytest:
# with sync_playwright() as playwright:
#     run(playwright)


import pytest

# Аддон  pytest-playwright реализует несколько фикстур
# Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")


# Пропустить тест браузером:
@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")


# Запуск в определенном браузере:
@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")

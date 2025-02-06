# import pytest
# import re
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         },
#         **browser_context_args,
#         "storage_state": {
#             "cookies": [
#                 {
#                     "name": "pola",
#                     "value": "sd4fFfv!x_cfcPola",
#                     "url": "https://demo.playwright.dev/todomvc/#/"  # Замените на нужный URL
#                 },
#             ]
#         },
#     }

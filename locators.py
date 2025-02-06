# PlayWright method for locators:
# схема page.locator(selector, **kwargs)

# CSS: tagname[attribute='attribute value']
# page.locator("css=button").click()
# page.locator("#new-todo").click()
# page.locator(".new-todo").click()
# page.locator("css=.first-class.another-class").click()
# page.locator("[placeholder='Your email address']").click()
# page.locator("input[placeholder='Your email address']").click()
# page.locator(".container p").click()
# page.locator("td:right-of(td p:text('Software engineer'))")
# page.locator("td:left-of(td p:text('Software engineer'))")
# page.locator("td:above(td p:text('Consultant'))")
# page.locator("td:below(td p:text('Consultant'))")
# page.locator("td:near(td p:text('Consultant'))")
# page.locator('button:has-text("Log in"), button:has-text("Sign in")').click()
# page.locator("button").locator("nth=0").click()
# page.locator("button").locator("nth=-1").click()
# page.locator("button:visible").click()
# page.locator('div:has-text("Card")').click()

# XPath: //tag_name[@attribute_name ='Value of attribute']
# page.locator("xpath=//button").click()
# page.locator("//*[@id='new-todo']").click()
# page.locator("//*[@class='new-todo']").click()
# page.locator("xpath=//div[contains(@class, 'first-class') and contains(@class, 'another-class')]").click()
# page.locator("//*[@placeholder='Your email address']").click()
# page.locator("//input[@placeholder='Your email address']").click()
# page.locator(".container > p").click()

# Playwright locators get_by_*:
# page.get_by_text(text, **kwargs)
# page.get_by_text("switch checkbox").click()
# page.get_by_text("switch checkbox",exact=True).click()
# page.get_by_label("Email address").fill("qa@example.com")
# page.get_by_placeholder("password")
# page.get_by_test_id('todo-title').click()
# page.get_by_alt_text('logo').click()
# page.get_by_title("username").fill("Anton")
# page.get_by_role("button", name="Submit").click()


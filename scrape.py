from playwright.sync_api import sync_playwright


def run(playwright) -> None:

    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")

    print(page.title())
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

import pytest
from playwright.sync_api import sync_playwright, Playwright, Browser
from pages.kiwi_homepage import KiwiHomepage


@pytest.fixture(scope="session")
def playwright_instance():
    """Initializes and yields the Playwright instance for the session."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    return playwright_instance.chromium.launch(headless=False)

@pytest.fixture(scope="function")
def page(browser: Browser):
    """Creates a new page (tab) for each test function."""
    page = browser.new_page()
    page.set_default_timeout(10000) 
    yield page
    page.close()
    
@pytest.fixture
def kiwi_homepage(page):
    return KiwiHomepage(page)
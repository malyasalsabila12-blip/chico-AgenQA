import pytest
import allure
from playwright.sync_api import sync_playwright
from config import config

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=config.HEADLESS)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    # Professional Practice: Context isolation and log capturing
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    
    # Storage for logs
    console_logs = []
    network_errors = []

    page = context.new_page()
    
    # Attach listeners for diagnostics
    page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text}"))
    page.on("requestfailed", lambda request: network_errors.append(f"FAILED: {request.url} - {request.failure.error_text}"))

    yield page
    
    # Logic to attach logs on failure is handled in the hook below
    page.close()
    context.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook checks if a test failed and attaches evidence
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            # 1. Capture Screenshot
            allure.attach(
                page.screenshot(full_page=True),
                name="Final State Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            # 2. Capture Page Source
            allure.attach(
                page.content(),
                name="DOM HTML Source",
                attachment_type=allure.attachment_type.HTML
            )

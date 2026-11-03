from playwright.sync_api import Page, expect
import allure
import re

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self._first_name = page.locator("#first-name")
        self._last_name = page.locator("#last-name")
        self._zip_code = page.locator("#postal-code")
        self._continue_button = page.locator("#continue")
        self._finish_button = page.locator("#finish")
        self._checkout_container = page.locator("#checkout_summary_container")
        self._complete_header = page.locator(".complete-header")

    @allure.step("Enter checkout information: {first_name} {last_name}")
    def enter_info(self, first_name: str, last_name: str, zip_code: str):
        self._first_name.fill(first_name)
        self._last_name.fill(last_name)
        self._zip_code.fill(zip_code)
        self._continue_button.click()
        expect(self.page).to_have_url(re.compile(r".*/checkout-step-two.html"))

    @allure.step("Finish checkout")
    def finish(self):
        self._finish_button.click()
        expect(self.page).to_have_url(re.compile(r".*/checkout-complete.html"))

    @allure.step("Verify order completion message")
    def verify_complete(self, expected_message="Thank you for your order!"):
        expect(self._complete_header).to_have_text(expected_message)

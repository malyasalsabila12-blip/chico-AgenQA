from playwright.sync_api import Page, expect
import allure

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self._username_field = page.locator("#user-name")
        self._password_field = page.locator("#password")
        self._login_button = page.locator("#login-button")
        self._error_message = page.locator("[data-test='error']")

    @allure.step("Navigate to Login Page")
    def navigate(self, url: str):
        self.page.goto(url)

    @allure.step("Login with credentials: {username}/{password}")
    def login(self, username: str, password: str):
        self._username_field.fill(username)
        self._password_field.fill(password)
        self._login_button.click()

    @allure.step("Verify error message visible")
    def verify_error_displayed(self):
        expect(self._error_message).to_be_visible()

    @allure.step("Get error message text")
    def get_error_message(self):
        return self._error_message.text_content()

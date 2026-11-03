from playwright.sync_api import Page, expect
import allure
import re

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self._checkout_button = page.locator("#checkout")
        self._cart_items = page.locator(".cart_item")

    @allure.step("Proceed to checkout")
    def checkout(self):
        self._checkout_button.click()
        expect(self.page).to_have_url(re.compile(r".*/checkout-step-one.html"))

    @allure.step("Verify item '{product_name}' is in cart")
    def verify_item_visible(self, product_name: str):
        expect(self._cart_items.filter(has_text=product_name)).to_be_visible()

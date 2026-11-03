from playwright.sync_api import Page, expect
import allure
import re

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self._header_title = page.locator(".title")
        self._cart_link = page.locator(".shopping_cart_link")
        self._burger_menu = page.locator("#react-burger-menu-btn")
        self._logout_link = page.locator("#logout_sidebar_link")
        self._inventory_items = page.locator(".inventory_item")

    @allure.step("Add product '{product_name}' to cart")
    def add_item_to_cart(self, product_name: str):
        item = self._inventory_items.filter(has_text=product_name)
        item.locator("button:has-text('Add to cart')").click()

    @allure.step("Open shopping cart")
    def go_to_cart(self):
        self._cart_link.click()
        expect(self.page).to_have_url(re.compile(r".*/cart.html"))

    @allure.step("Logout from application")
    def logout(self):
        self._burger_menu.click()
        expect(self._logout_link).to_be_visible()
        self._logout_link.click()
        expect(self.page).to_have_url(re.compile(r".*/index.html|.*/"))

    @allure.step("Verify on Inventory Page")
    def verify_on_page(self):
        expect(self._header_title).to_have_text("Products")
        expect(self.page).to_have_url(re.compile(r".*/inventory.html"))

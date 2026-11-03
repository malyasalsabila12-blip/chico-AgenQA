from playwright.sync_api import Page, expect
import allure
import pytest
import re
import os
import sys

# Add parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Professional Practice: Import central configuration
from config import config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

test_cases = [
    "Verify standard_user can log in successfully with correct credentials.",
    "Verify standard_user can add 'Sauce Labs Backpack' to cart from product page.",
    "Verify standard_user can navigate to cart and see added item.",
    "Verify standard_user can proceed to checkout after adding items to cart.",
    "Verify standard_user can fill in checkout information (First Name, Last Name, Zip/Postal Code) and continue.",
    "Verify standard_user can complete the order successfully after reviewing items.",
    "Verify standard_user can log out successfully from the product page.",
    "Verify standard_user can view product details page after clicking on a product.",
    "Verify that clicking on the shopping cart icon redirects to the cart page.",
    "Verify error message is displayed when logging in with invalid username and valid password.",
    "Verify error message is displayed when logging in with valid username and invalid password.",
    "Verify error message is displayed when logging in with invalid username and invalid password.",
    "Verify error message is displayed when logging in with empty username and empty password.",
    "Verify locked_out_user cannot log in and sees specific error message.",
    "Verify user cannot proceed to checkout without adding any items to cart.",
    "Verify error message is displayed when checkout information (First Name) is missing."
]

@allure.feature('SauceDemo E-commerce Features')
@pytest.mark.parametrize('test_case', test_cases)
def test_saucedemo_scenario(page: Page, test_case: str):
    allure.dynamic.title(test_case)
    allure.dynamic.description(f'Executing test case: {test_case}')

    # Initialize Page Objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    try:
        # --- Authentication Tests ---
        if 'log in successfully with correct credentials' in test_case.lower() and 'standard_user' in test_case.lower():
            login_page.navigate(config.BASE_URL)
            login_page.login(config.STANDARD_USER, config.PASSWORD)
            inventory_page.verify_on_page()
            allure.attach(page.screenshot(full_page=True), name='Successful Login', attachment_type=allure.attachment_type.PNG)

        elif 'error message is displayed when logging in with invalid username and valid password' in test_case.lower():
            login_page.navigate(config.BASE_URL)
            login_page.login('invalid_user', config.PASSWORD)
            login_page.verify_error_displayed()
            expect(login_page._error_message).to_have_text('Epic sadface: Username and password do not match any user in this service')
            allure.attach(page.screenshot(full_page=True), name='Invalid Username Login', attachment_type=allure.attachment_type.PNG)

        elif 'locked_out_user cannot log in' in test_case.lower():
            login_page.navigate(config.BASE_URL)
            login_page.login(config.LOCKED_OUT_USER, config.PASSWORD)
            login_page.verify_error_displayed()
            expect(login_page._error_message).to_have_text('Epic sadface: Sorry, this user has been locked out.')
            allure.attach(page.screenshot(full_page=True), name='Locked Out User', attachment_type=allure.attachment_type.PNG)

        # --- Functional Tests ---
        elif 'add \'sauce labs backpack\' to cart' in test_case.lower():
            login_page.navigate(config.BASE_URL)
            login_page.login(config.STANDARD_USER, config.PASSWORD)
            inventory_page.add_item_to_cart('Sauce Labs Backpack')
            expect(page.locator('.shopping_cart_badge')).to_have_text('1')
            allure.attach(page.screenshot(full_page=True), name='Add Item', attachment_type=allure.attachment_type.PNG)

        elif 'navigate to cart and see added item' in test_case.lower():
            login_page.navigate(config.BASE_URL)
            login_page.login(config.STANDARD_USER, config.PASSWORD)
            inventory_page.add_item_to_cart('Sauce Labs Backpack')
            inventory_page.go_to_cart()
            cart_page.verify_item_visible('Sauce Labs Backpack')
            allure.attach(page.screenshot(full_page=True), name='Cart View', attachment_type=allure.attachment_type.PNG)

        elif 'complete the order successfully' in test_case.lower():
            login_page.navigate(config.BASE_URL)
            login_page.login(config.STANDARD_USER, config.PASSWORD)
            inventory_page.add_item_to_cart('Sauce Labs Backpack')
            inventory_page.go_to_cart()
            cart_page.checkout()
            checkout_page.enter_info('John', 'Doe', '12345')
            checkout_page.finish()
            checkout_page.verify_complete()
            allure.attach(page.screenshot(full_page=True), name='Order Complete', attachment_type=allure.attachment_type.PNG)

        elif 'log out successfully' in test_case.lower():
            login_page.navigate(config.BASE_URL)
            login_page.login(config.STANDARD_USER, config.PASSWORD)
            inventory_page.logout()
            expect(login_page._login_button).to_be_visible()
            allure.attach(page.screenshot(full_page=True), name='Logout Success', attachment_type=allure.attachment_type.PNG)

        elif 'error message is displayed when checkout information (first name) is missing' in test_case.lower():
            login_page.navigate(config.BASE_URL)
            login_page.login(config.STANDARD_USER, config.PASSWORD)
            inventory_page.add_item_to_cart('Sauce Labs Backpack')
            inventory_page.go_to_cart()
            cart_page.checkout()
            page.fill('#last-name', 'Doe')
            page.fill('#postal-code', '12345')
            page.click('#continue')
            expect(page.locator('[data-test="error"]')).to_have_text('Error: First Name is required')
            allure.attach(page.screenshot(full_page=True), name='Missing Info Error', attachment_type=allure.attachment_type.PNG)

        else:
            pytest.skip(f"Test case implementation in progress: {test_case}")

    except Exception as e:
        allure.attach(page.screenshot(full_page=True), name='Failure Error', attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test Case Failed: {str(e)}")

from typing import List, Dict

def generate_test_cases(url: str, breakdown: Dict[str, int]) -> List[str]:
    """
    Generates test cases for a given URL based on the specified breakdown.
    """
    print(f"Generating {sum(breakdown.values())} test cases for {url}...")
    test_cases = []

    # Happy Path Test Cases (7)
    if breakdown.get("happy", 0) > 0:
        test_cases.extend([
            "Verify standard_user can log in successfully with correct credentials.",
            "Verify standard_user can add 'Sauce Labs Backpack' to cart from product page.",
            "Verify standard_user can navigate to cart and see added item.",
            "Verify standard_user can proceed to checkout after adding items to cart.",
            "Verify standard_user can fill in checkout information (First Name, Last Name, Zip/Postal Code) and continue.",
            "Verify standard_user can complete the order successfully after reviewing items.",
            "Verify standard_user can log out successfully from the product page.",
            "Verify standard_user can view product details page after clicking on a product.",
            "Verify that clicking on the shopping cart icon redirects to the cart page."
        ][:breakdown["happy"]])

    # Negative Test Cases (7)
    if breakdown.get("negative", 0) > 0:
        test_cases.extend([
            "Verify error message is displayed when logging in with invalid username and valid password.",
            "Verify error message is displayed when logging in with valid username and invalid password.",
            "Verify error message is displayed when logging in with invalid username and invalid password.",
            "Verify error message is displayed when logging in with empty username and empty password.",
            "Verify locked_out_user cannot log in and sees specific error message.",
            "Verify user cannot proceed to checkout without adding any items to cart.",
            "Verify error message is displayed when checkout information (First Name) is missing."
        ][:breakdown["negative"]])

    # Boundary Test Cases (3)
    if breakdown.get("boundary", 0) > 0:
        test_cases.extend([
            "Verify username/password fields handle maximum allowed characters (e.g., very long strings if possible without breaking input).",
            "Verify product sorting (e.g., A-Z, Z-A) works correctly for minimum (0) or maximum (all) products visible.",
            "Verify cart quantity updates correctly when adding/removing the same item multiple times (e.g., 0 -> 1 -> 0 or 99 -> 100)."
        ][:breakdown["boundary"]])

    # Edge Test Cases (2)
    if breakdown.get("edge", 0) > 0:
        test_cases.extend([
            "Verify behavior when attempting to access a secured page directly without authentication.",
            "Verify behavior when JavaScript is disabled (if applicable and testable through Playwright)."
        ][:breakdown["edge"]])

    return test_cases

if __name__ == "__main__":
    # Example usage for saucedemo.com
    sauce_url = "https://www.saucedemo.com/"
    test_breakdown = {"happy": 7, "negative": 7, "boundary": 3, "edge": 2}
    test_cases = generate_test_cases(sauce_url, test_breakdown)
    for i, test_case in enumerate(test_cases):
        print(f"Test Case {i+1}: {test_case}")
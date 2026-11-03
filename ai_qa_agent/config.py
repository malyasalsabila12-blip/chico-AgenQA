import os

class Config:
    """
    Centralized configuration for the QA Automation Framework.
    Values are pulled from environment variables, with defaults for local dev.
    """
    # Environment & URLs
    BASE_URL = os.getenv("SAUCEDEMO_URL", "https://www.saucedemo.com/")
    
    # Credentials (Use environment variables in CI/CD)
    STANDARD_USER = os.getenv("SAUCE_USERNAME", "standard_user")
    PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    LOCKED_OUT_USER = os.getenv("SAUCE_LOCKED_USER", "locked_out_user")
    
    # Framework Settings
    HEADLESS = os.getenv("BROWSER_HEADLESS", "True").lower() == "true"
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30000"))  # 30 seconds
    
    # Reporting
    ALLURE_RESULTS_DIR = os.path.join(os.getcwd(), "allure-results")

# Initialize a global config instance
config = Config()

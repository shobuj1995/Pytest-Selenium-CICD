import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# ✅ Skip SSL certificate checks if needed
os.environ['WDM_SSL_VERIFY'] = '0'


def get_driver(browser_name):
    driver = None
    is_ci = os.getenv("GITHUB_ACTIONS") == "true"  # Detect GitHub Actions

    if browser_name.lower() == "chrome":
        options = ChromeOptions()

        # Headless mode only in GitHub Actions
        if is_ci:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        options.add_argument("--incognito")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name.lower() == "firefox":
        options = FirefoxOptions()

        if is_ci:
            options.add_argument("--headless")

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    elif browser_name.lower() == "edge":
        options = EdgeOptions()

        if is_ci:
            options.add_argument("--headless")

        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

    elif browser_name.lower() == "safari":
        if not sys.platform.startswith("darwin"):
            raise Exception("Safari is only supported on macOS.")
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)

    if not is_ci:  # Don’t maximize window in headless mode
        driver.maximize_window()

    return driver

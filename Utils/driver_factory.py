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

    if browser_name.lower() == "chrome":
        options = ChromeOptions()

        # Enable incognito mode
        options.add_argument("--incognito")

        # Disable password manager & credential service popups
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        # Disable automation flags and infobars
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-blink-features=AutomationControlled")

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name.lower() == "firefox":
        options = FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    elif browser_name.lower() == "edge":
        options = EdgeOptions()
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

    elif browser_name.lower() == "safari":
        if not sys.platform.startswith("darwin"):
            raise Exception("Safari is only supported on macOS.")
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # ✅ Set global waits and maximize window
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
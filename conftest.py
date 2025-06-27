import json
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.ie.service import Service
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Utils.driver_factory import get_driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests"
    )

@pytest.fixture
def driver():
    driver = get_driver()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def config():
    return load_config()


# This is the process how can we do it by hardcoding the driver
# @pytest.fixture(scope="function")
# def browserInstance(request):
#     browser_name=request.config.getoption("--browser_name")
#     service_obj=Service()
#     if browser_name=="chrome":
#         driver=webdriver.Chrome(service=service_obj)
#         driver.implicitly_wait(4)
#     yield driver
#     driver.quit
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")
    driver = None

    if browser_name.lower() == "chrome":
        chrome_options = ChromeOptions()
        service_obj = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.maximize_window()

    elif browser_name.lower() == "firefox":
        firefox_options = FirefoxOptions()
        service_obj = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_obj, options=firefox_options)
        driver.maximize_window()

    elif browser_name.lower() == "edge":
        edge_options = EdgeOptions()
        service_obj = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service_obj, options=edge_options)
        driver.maximize_window()

    elif browser_name.lower() == "safari":
        if not sys.platform.startswith("darwin"):
            raise Exception("Safari is only supported on macOS.")
        driver = webdriver.Safari()  # Safari does not need a driver manager
        driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(4)
    yield driver
    driver.close()





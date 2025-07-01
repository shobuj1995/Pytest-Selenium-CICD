import json
import os
import pytest
from Utils.driver_factory import get_driver

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    driver = get_driver(browser_name)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def load_data():
    data_path = os.path.join(
        os.path.dirname(__file__),
        "project2_automation", "data", "testdata.json"
    )
    with open(data_path) as f:
        return json.load(f)

@pytest.fixture
def login_data_row(request, load_data):
    return load_data["data"][request.param]

def pytest_generate_tests(metafunc):
    if "login_data_row" in metafunc.fixturenames:
        data_path = os.path.join(
            os.path.dirname(__file__),
            "project2_automation", "data", "testdata.json"
        )
        with open(data_path) as f:
            data = json.load(f)
        test_list = data["data"]
        indices = list(range(len(test_list)))
        metafunc.parametrize("login_data_row", indices, indirect=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Take a screenshot and embed in HTML report if test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Screenshot setup
            reports_dir = os.path.join(os.getcwd(), "project2_automation", "Reports", "screenshots")
            os.makedirs(reports_dir, exist_ok=True)

            safe_test_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            file_name = os.path.join(reports_dir, f"{safe_test_name}.png")

            try:
                driver = item.funcargs['browserInstance']
                driver.get_screenshot_as_file(file_name)

                # ✅ Path relative to HTML report
                html_report_path = item.config.option.htmlpath
                rel_path = os.path.relpath(file_name, os.path.dirname(html_report_path))

                html = f'<div><img src="{rel_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))

            except Exception as e:
                print(f"[WARNING] Could not capture screenshot: {e}")

            report.extra = extra
# ___________________________________________________________________________________________________________________________
# import json
# import pytest
# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.ie.service import Service
# import sys
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.edge.options import Options as EdgeOptions
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# from Utils.driver_factory import get_driver
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome", help="Browser to run tests"
#     )
#
# @pytest.fixture
# def driver():
#     driver = get_driver()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
# def load_config():
#     with open("config.json", "r") as f:
#         return json.load(f)
#
# @pytest.fixture(scope="session")
# def config():
#     return load_config()
#
#
# # This is the process how can we do it by hardcoding the driver
# # @pytest.fixture(scope="function")
# # def browserInstance(request):
# #     browser_name=request.config.getoption("--browser_name")
# #     service_obj=Service()
# #     if browser_name=="chrome":
# #         driver=webdriver.Chrome(service=service_obj)
# #         driver.implicitly_wait(4)
# #     yield driver
# #     driver.quit
# @pytest.fixture(scope="function")
# def browserInstance(request):
#     browser_name = request.config.getoption("--browser_name")
#     driver = None
#
#     if browser_name.lower() == "chrome":
#         chrome_options = ChromeOptions()
#         service_obj = ChromeService(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#         driver.maximize_window()
#
#     elif browser_name.lower() == "firefox":
#         firefox_options = FirefoxOptions()
#         service_obj = FirefoxService(GeckoDriverManager().install())
#         driver = webdriver.Firefox(service=service_obj, options=firefox_options)
#         driver.maximize_window()
#
#     elif browser_name.lower() == "edge":
#         edge_options = EdgeOptions()
#         service_obj = EdgeService(EdgeChromiumDriverManager().install())
#         driver = webdriver.Edge(service=service_obj, options=edge_options)
#         driver.maximize_window()
#
#     elif browser_name.lower() == "safari":
#         if not sys.platform.startswith("darwin"):
#             raise Exception("Safari is only supported on macOS.")
#         driver = webdriver.Safari()  # Safari does not need a driver manager
#         driver.maximize_window()
#
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}")
#
#     driver.implicitly_wait(4)
#     yield driver
#     driver.close()
#
#
#
#

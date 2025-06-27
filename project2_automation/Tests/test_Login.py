import pytest
from project2_automation.Pages.LoginPage import LoginPage  # Make sure the path is correct
from conftest import driver


def test_login_valid(browserInstance, config):
    driver=browserInstance
    driver.get(config["rahuls"]["url"])  # or config["demoqa"]["url"]
    login_page = LoginPage(driver)

    # Perform login
    home_page = login_page.login(
        config["rahuls"]["username"], config["rahuls"]["password"]
    )

    # Assert dashboard is displayed (assuming it returns a page object)
    assert home_page.is_home_displayed()

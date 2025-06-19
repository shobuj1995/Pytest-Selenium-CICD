import pytest

from Pages.LoginPage import LoginPage
from conftest import load_config


def test_login_valid(driver, config):
    driver.get(config["url"])
    login_page = LoginPage(driver)
    dashboard=login_page.login(config["username"], config["password"])
    assert dashboard.is_dashboard_displayed()

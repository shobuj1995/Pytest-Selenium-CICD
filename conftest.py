import json

import pytest
from Utils.driver_factory import get_driver

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



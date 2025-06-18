import pytest
from Utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

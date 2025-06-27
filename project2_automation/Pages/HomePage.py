from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.success_banner = (By.CSS_SELECTOR, ".navbar-nav")  # Or change as needed

    def is_home_displayed(self):
        return self.driver.find_element(*self.success_banner).is_displayed()

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.DashboardPage import DashboardPage  # Import the new page

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        # Return new page object for Dashboard
        return DashboardPage(self.driver)

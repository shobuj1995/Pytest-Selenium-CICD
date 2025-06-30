from selenium.webdriver.common.by import By

from project2_automation.Pages.BasePage import BasePage
from project2_automation.Pages.HomePage import HomePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signin_button = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()
        return HomePage(self.driver)
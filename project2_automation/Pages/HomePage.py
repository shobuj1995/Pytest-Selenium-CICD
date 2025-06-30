from selenium.webdriver.common.by import By

from project2_automation.Pages.BasePage import BasePage
from project2_automation.Pages.Checkout_Confirmation import Checkout_Confirmation
from project2_automation.Pages.ShopPage import ShopPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.success_banner = (By.CSS_SELECTOR, ".navbar-nav")
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")

    def is_home_displayed(self):
        return self.driver.find_element(*self.success_banner).is_displayed()
    def navigate_to_shoppage(self):
        self.driver.find_element(*self.shop_link).click()
        return ShopPage(self.driver)
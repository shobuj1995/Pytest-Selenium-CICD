class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def enter_text(self, by_locator, text):
        self.driver.find_element(*by_locator).clear()
        self.driver.find_element(*by_locator).send_keys(text)

    def get_text(self, by_locator):
        return self.driver.find_element(*by_locator).text

    def is_visible(self, by_locator):
        element = self.driver.find_element(*by_locator)
        return element.is_displayed()

    def getTitle(self):
        return self.driver.title
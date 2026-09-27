from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.title_span = (By.CLASS_NAME, "title")

    def get_current_url(self):
        return self.driver.current_url

    def get_title_text(self):
        return self.driver.find_element(*self.title_span).text
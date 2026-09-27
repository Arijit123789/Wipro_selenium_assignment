from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        # Define web element locators
        self.name_field = (By.CSS_SELECTOR, "div.form-group > input#name")
        self.email_field = (By.CSS_SELECTOR, "div.form-group > input#email")
        self.phone_field = (By.CSS_SELECTOR, "div.form-group > input#phone")

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def enter_name(self, name):
        element = self.driver.find_element(*self.name_field)
        element.clear()
        element.send_keys(name)

    def enter_email(self, email):
        element = self.driver.find_element(*self.email_field)
        element.clear()
        element.send_keys(email)

    def enter_phone(self, phone):
        element = self.driver.find_element(*self.phone_field)
        element.clear()
        element.send_keys(phone)
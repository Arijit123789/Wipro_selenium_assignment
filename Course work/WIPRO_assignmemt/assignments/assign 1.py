from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # 1. Navigate to SauceDemo
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # 2. Username field using By.ID
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    # 3. Password field using By.NAME
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("secret_sauce")

    # 4. Login button using By.XPATH
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_button.click()

    # 5. Validation: Assert URL contains '/inventory.html'
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    current_url = driver.current_url
    assert "/inventory.html" in current_url, f"Expected '/inventory.html' in URL, but got: {current_url}"

    print("Assignment 1 Passed: Successfully logged in and validated URL.")

finally:
    driver.quit()
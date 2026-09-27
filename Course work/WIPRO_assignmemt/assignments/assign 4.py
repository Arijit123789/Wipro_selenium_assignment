from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    # 1. Trigger and accept basic Alert
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.accept()
    assert "You successfully clicked an alert" in driver.find_element(By.ID, "result").text

    # 2. Trigger and dismiss Confirm Box
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    confirm = WebDriverWait(driver, 5).until(EC.alert_is_present())
    confirm.dismiss()
    assert "You clicked: Cancel" in driver.find_element(By.ID, "result").text

    # 3. Trigger Prompt Box, enter text, and accept
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    prompt = WebDriverWait(driver, 5).until(EC.alert_is_present())
    prompt.send_keys("Selenium Automation Input")
    prompt.accept()
    assert "You entered: Selenium Automation Input" in driver.find_element(By.ID, "result").text

    print("Assignment 4 Passed: All alerts handled successfully.")

finally:
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Name - Child Node using CSS
name = driver.find_element(By.CSS_SELECTOR, "div.form-group > input#name")
name.send_keys("Arghadeep")

# Email - Child Node using CSS
email = driver.find_element(By.CSS_SELECTOR, "div.form-group > input#email")
email.send_keys("arghadeep@example.com")

# Phone - Child Node using CSS
phone = driver.find_element(By.CSS_SELECTOR, "div.form-group > input#phone")
phone.send_keys("9876543210")

print("Name entered successfully")
print("Email entered successfully")
print("Phone entered successfully")

input("Press Enter to close the browser...")

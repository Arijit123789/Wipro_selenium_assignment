from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/tables")
    driver.maximize_window()

    target_name = "Smith"
    due_value = None

    # Iterate through each row of the table
    rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
    for row in rows:
        last_name_col = row.find_element(By.XPATH, "./td[1]").text
        if target_name in last_name_col:
            # Column 4 corresponds to 'Due' / Price
            due_value = row.find_element(By.XPATH, "./td[4]").text
            break

    assert due_value is not None, f"Target row with name '{target_name}' not found."
    print(f"Assignment 5 Passed: Due amount for {target_name} is {due_value}")

finally:
    driver.quit()
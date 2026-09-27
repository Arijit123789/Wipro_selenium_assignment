from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # 1. Navigate to a dynamic loading example page
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.maximize_window()

    # 2. Click the 'Start' button to trigger the dynamic content load
    start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
    start_button.click()

    # 3. Explicit Wait: wait until the element containing text is visible
    finish_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
    )

    # 4. Validate the revealed text
    revealed_text = finish_element.text
    assert revealed_text == "Hello World!", f"Expected 'Hello World!', but found '{revealed_text}'"

    print(f"Assignment 2 Passed: Dynamically loaded text revealed -> '{revealed_text}'")

finally:
    driver.quit()
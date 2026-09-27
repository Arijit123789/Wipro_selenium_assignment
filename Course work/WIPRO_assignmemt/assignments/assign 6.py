from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.maximize_window()

    # Part 1: IFrames
    driver.get("https://the-internet.herokuapp.com/iframe")
    
    # Close any modal if present, then switch into iframe
    driver.switch_to.frame("mce_0_ifr")
    editor_body = driver.find_element(By.ID, "tinymce")
    editor_body.clear()
    editor_body.send_keys("Automating inside an iframe!")
    
    # Switch back to main DOM layout
    driver.switch_to.default_content()

    # Part 2: Windows / Tabs
    driver.get("https://the-internet.herokuapp.com/windows")
    original_window = driver.current_window_handle

    # Click to open new tab
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)

    # Switch to the new tab
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    print(f"New tab title: {driver.title}")
    assert "New Window" in driver.title

    # Close new tab and return to the original window
    driver.close()
    driver.switch_to.window(original_window)
    print("Assignment 6 Passed: Context returned to main page successfully.")

finally:
    driver.quit()
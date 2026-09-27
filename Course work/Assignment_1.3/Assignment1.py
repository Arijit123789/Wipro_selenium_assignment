from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize browser
driver.maximize_window()


# =========================================================
# 1. LOCATE ELEMENT USING ID
# =========================================================

name = driver.find_element(By.ID, "name")
name.send_keys("John")

print("1. By.ID      : Name field found")


# =========================================================
# 2. LOCATE ELEMENT USING NAME
# =========================================================

# The page does not have a useful form field with a name
# attribute, so we use the meta element with name="viewport".

viewport = driver.find_element(By.NAME, "viewport")

print("2. By.NAME    : Element found =", viewport.tag_name)


# =========================================================
# 3. LOCATE ELEMENT USING TAG NAME
# =========================================================

inputs = driver.find_elements(By.TAG_NAME, "input")

print("3. By.TAG_NAME : Number of input elements =", len(inputs))


# =========================================================
# 4. LOCATE ELEMENT USING LINK TEXT
# =========================================================

home = driver.find_element(By.LINK_TEXT, "Home")

print("4. By.LINK_TEXT: Home link found")


# =========================================================
# 5. LOCATE ELEMENT USING CLASS NAME
# =========================================================

element = driver.find_element(By.CLASS_NAME, "form-control")

print("5. By.CLASS_NAME: Element found =", element.get_attribute("placeholder"))


# Keep browser open
input("Press Enter to close the browser...")

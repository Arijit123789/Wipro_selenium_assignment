from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize browser
driver.maximize_window()

# Find all links on the webpage
links = driver.find_elements(By.TAG_NAME, "a")

# Print number of links
print("Total number of links:", len(links))

# Print text of every link
print("\nLink texts:")

for link in links:
    text = link.text
    if text:
        print(text)

# Keep browser open
input("\nPress Enter to close the browser...")

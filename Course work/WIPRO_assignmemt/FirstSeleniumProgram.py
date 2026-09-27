from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.google.com")
pageTitle=driver.title
print(pageTitle)
print(driver.current_url) 
language_link= driver.find_elements(By.LINK_TEXT,"English")
print(language_link)
driver.quit()
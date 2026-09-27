from selenium import webdriver
from page.login_page import LoginPage
from page.dashboard_page import DashboardPage

driver = webdriver.Chrome()

try:
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Assertions stay inside the test script, separated from page models
    assert "/inventory.html" in dashboard_page.get_current_url()
    assert dashboard_page.get_title_text() == "Products"
    print("Assignment 7 Passed: POM pattern verified.")

finally:
    driver.quit()
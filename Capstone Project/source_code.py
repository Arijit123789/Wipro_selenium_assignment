from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_ecommerce_purchase():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-email").send_keys("test@example.com")
    driver.find_element(By.ID, "input-password").send_keys("test123")
    driver.find_element(
        By.CSS_SELECTOR, "input[type='submit']"
    ).click()
    time.sleep(2)
    search = driver.find_element(By.NAME, "search")
    search.send_keys("MacBook")
    driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn-default.btn-lg"
    ).click()
    time.sleep(3)
    driver.save_screenshot(
        "screenshots/01_product_search.png"
    )
    driver.find_element(By.LINK_TEXT, "MacBook").click()
    time.sleep(2)
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(3)
    driver.save_screenshot(
        "screenshots/02_product_added.png"
    )
    driver.find_element(By.ID, "cart-total").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "View Cart").click()
    time.sleep(3)
    quantity = driver.find_element(
        By.CSS_SELECTOR, "input[name^='quantity']"
    )
    quantity.clear()
    quantity.send_keys("2")

    driver.find_element(
        By.CSS_SELECTOR,
        "button[data-original-title='Update']"
    ).click()
    time.sleep(3)
    assert "MacBook" in driver.page_source
    quantity = driver.find_element(
        By.CSS_SELECTOR, "input[name^='quantity']"
    )
    assert quantity.get_attribute("value") == "2"
    driver.save_screenshot(
        "screenshots/03_cart_verified.png"
    )
    print("Product search successful")
    print("Product added to cart")
    print("Quantity updated to 2")
    print("Cart verification successful")
    driver.quit()
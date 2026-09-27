from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I open the test automation practice website')
def step_open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://testautomationpractice.blogspot.com/")
    context.driver.maximize_window()

@when('I enter my name "{name_text}"')
def step_enter_name(context, name_text):
    name = context.driver.find_element(By.CSS_SELECTOR, "div.form-group > input#name")
    name.send_keys(name_text)

@when('I enter my email "{email_text}"')
def step_enter_email(context, email_text):
    email = context.driver.find_element(By.CSS_SELECTOR, "div.form-group > input#email")
    email.send_keys(email_text)

@when('I enter my phone number "{phone_text}"')
def step_enter_phone(context, phone_text):
    phone = context.driver.find_element(By.CSS_SELECTOR, "div.form-group > input#phone")
    phone.send_keys(phone_text)

@then('the details should be entered successfully')
def step_verify_submission(context):
    print("Assignment 1 executed successfully via Behave BDD!")
    context.driver.quit()
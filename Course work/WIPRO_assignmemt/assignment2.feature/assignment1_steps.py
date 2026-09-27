from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I open the test automation practice website for data-driven testing')
def step_open_datadriven_site(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com")
    context.driver.maximize_window()

@when('I enter the username "{name}"')
def step_enter_data_name(context, name):
    name_field = context.driver.find_element(By.CSS_SELECTOR, "div.form-group > input#name")
    name_field.clear()
    name_field.send_keys(name)

@when('I enter the user email "{email}"')
def step_enter_data_email(context, email):
    email_field = context.driver.find_element(By.CSS_SELECTOR, "div.form-group > input#email")
    email_field.clear()
    email_field.send_keys(email)

@when('I enter the user phone "{phone}"')
def step_enter_data_phone(context, phone):
    phone_field = context.driver.find_element(By.CSS_SELECTOR, "div.form-group > input#phone")
    phone_field.clear()
    phone_field.send_keys(phone)

@then('the test data should be processed successfully')
def step_verify_datadriven(context):
    print("Test data processed successfully for this row!")
    context.driver.quit()
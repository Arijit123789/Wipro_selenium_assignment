from behave import given, when, then
from selenium import webdriver
from feature.page.form_page import FormPage
@given('I navigate to the test automation practice website using POM')
def step_navigate_pom(context):
    context.driver = webdriver.Chrome()
    # Initialize the Page Object
    context.form_page = FormPage(context.driver)
    context.form_page.open_page("https://testautomationpractice.blogspot.com/")

@when('I fill out the form with name "{name}", email "{email}", and phone "{phone}" using POM')
def step_fill_form_pom(context, name, email, phone):
    # Call methods from the Page Object model class
    context.form_page.enter_name(name)
    context.form_page.enter_email(email)
    context.form_page.enter_phone(phone)

@then('the form submission via POM should complete successfully')
def step_verify_pom(context):
    print("Assignment 3 Page Object Model test executed successfully!")
    context.driver.quit()
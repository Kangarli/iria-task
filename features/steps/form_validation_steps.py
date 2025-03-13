from behave import when, then
from selenium.webdriver.common.by import By
from features.steps.common_steps import *
from utils.screenshot import take_screenshot
import time
from utils.csv_reader import read_csv_data

valid_data = read_csv_data('data/valid_data.csv')
invalid_data = read_csv_data('data/invalid_data.csv')


@when('Fill the form with valid data')
def step_fill_valid_form(context):
    try:
        data = valid_data[0]
        context.driver.find_element(By.ID, "validationCustom01").send_keys(data['Name'])
        context.driver.find_element(By.ID, "validationCustom05").send_keys(data['Phone'])
        context.driver.find_element(By.NAME, "pickupdate").send_keys(data['Date'])
        context.driver.find_element(By.NAME, "payment").send_keys(data['PaymentMethod'])
    except Exception as e:
        take_screenshot(context.driver, "fill_valid_form_failure")
        raise e

@when('Fill the form with invalid data')
def step_fill_invalid_form(context):
    try:
        data = invalid_data[0]
        context.driver.find_element(By.ID, "validationCustom01").send_keys(data['Name'])
        context.driver.find_element(By.ID, "validationCustom05").send_keys(data['Phone'])
        context.driver.find_element(By.NAME, "pickupdate").send_keys(data['Date'])
    except Exception as e:
        take_screenshot(context.driver, "fill_invalid_form_failure")
        raise e

@when('Submit the form')
def step_submit_form(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
    except Exception as e:
        take_screenshot(context.driver, "submit_form_failure")
        raise e

@then('Should see a succes mesage')
def step_verify_success(context):
    try:
        assert "Thank you for validating your ticket" in context.driver.page_source
    except AssertionError as e:
        take_screenshot(context.driver, "verify_success_failure")
        raise e

@then('Should see appropriate error messages')
def step_verify_errors(context):
    try:
        assert "Please enter your Contact name." in context.driver.page_source
        assert "Please provide your Contact number." in context.driver.page_source
    except AssertionError as e:
        take_screenshot(context.driver, "verify_errors_failure")
        raise e

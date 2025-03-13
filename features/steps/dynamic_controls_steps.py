from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.steps.common_steps import *
from utils.screenshot import take_screenshot

@when('Check the checkbox')
def step_check_checkbox(context):
    try:
        checkbox = context.driver.find_element(By.ID, "checkbox").find_element(By.TAG_NAME, "input")
        if not checkbox.is_selected():
            checkbox.click()
    except Exception as e:
        take_screenshot(context.driver, "check_checkbox_failure")
        raise e

@when('Uncheck the checkbox')
def step_uncheck_checkbox(context):
    try:
        checkbox = context.driver.find_element(By.ID, "checkbox").find_element(By.TAG_NAME, "input")
        if checkbox.is_selected():
            checkbox.click()
    except Exception as e:
        take_screenshot(context.driver, "uncheck_checkbox_failure")
        raise e

@when('Remove checkbox button')
def step_click_remove_checkbox(context):
    try:
        context.driver.find_element(By.XPATH, "//button[normalize-space(text())='Remove']").click()
        WebDriverWait(context.driver, 5).until(
            EC.invisibility_of_element_located((By.ID, "checkbox"))
        )
    except Exception as e:
        take_screenshot(context.driver, "remove_checkbox_failure")
        raise e

@when('Enable the input field')
def step_enable_input(context):
    try:
        context.driver.find_element(By.XPATH, "//button[normalize-space(text())='Enable']").click()
        WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
        )
    except Exception as e:
        take_screenshot(context.driver, "enable_input_failure")
        raise e

@when('Disable the input field')
def step_disable_input(context):
    try:
        context.driver.find_element(By.XPATH, "//button[normalize-space(text())='Disable']").click()
        WebDriverWait(context.driver, 5).until(
            EC.element_attribute_to_include((By.CSS_SELECTOR, "input[type='text']"), "disabled")
        )
    except Exception as e:
        take_screenshot(context.driver, "disable_input_failure")
        raise e

@then('Should see the checkbox removed')
def step_verify_checkbox_removed(context):
    try:
        wait = WebDriverWait(context.driver, 5)
        wait.until(EC.invisibility_of_element_located((By.ID, "checkbox")))
        assert True
    except Exception as e:
        take_screenshot(context.driver, "verify_checkbox_removed_failure")
        raise e

@then('Should see the input field enabled')
def step_verify_input_enabled(context):
    try:
        input_field = context.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        assert input_field.is_enabled()
    except AssertionError as e:
        take_screenshot(context.driver, "verify_input_enabled_failure")
        raise e

@then('Should see the input field disabled')
def step_verify_input_disabled(context):
    try:
        input_field = context.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        assert not input_field.is_enabled()
    except AssertionError as e:
        take_screenshot(context.driver, "verify_input_disabled_failure")
        raise e

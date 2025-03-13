from behave import when, then
from selenium.webdriver.common.by import By
import time
from utils.screenshot import take_screenshot

@when('Extract values from the "Last Name" column')
def step_extract_last_names(context):
    try:
        context.last_names = [
            element.text.strip() for element in context.driver.find_elements(By.XPATH, '//table[@id="table1"]/tbody/tr/td[1]')
        ]
    except Exception as e:
        take_screenshot(context.driver, "extract_last_names_failure")
        raise e

@then('Validate the extracted values are ["Smith", "Bach", "Doe", "Conway"]')
def step_validate_last_names(context):
    expected_last_names = ["Smith", "Bach", "Doe", "Conway"]
    try:
        assert context.last_names == expected_last_names, f"Expected {expected_last_names}, but got {context.last_names}"
    except AssertionError as e:
        take_screenshot(context.driver, "validate_last_names_failure")
        raise e

@when('Count the rows in the table')
def step_count_rows(context):
    try:
        context.initial_row_count = len(context.driver.find_elements(By.XPATH, '//table[@id="table1"]/tbody/tr'))
    except Exception as e:
        take_screenshot(context.driver, "count_rows_failure")
        raise e

@when('Perform a "Delete" action on the first row')
def step_delete_first_row(context):
    try:
        delete_button = context.driver.find_element(By.XPATH, '//table[@id="table1"]/tbody/tr[1]//a[contains(@class, "btn-danger")]')
        delete_button.click()
        time.sleep(2)
    except Exception as e:
        take_screenshot(context.driver, "delete_first_row_failure")
        raise e

@then('Verify the row count is reduced by 1 after delete')
def step_verify_row_count(context):
    try:
        time.sleep(1)
        updated_row_count = len(context.driver.find_elements(By.XPATH, '//table[@id="table1"]/tbody/tr'))
        assert updated_row_count == context.initial_row_count - 1, \
            f"Expected {context.initial_row_count - 1} rows, but got {updated_row_count}"
    except AssertionError as e:
        take_screenshot(context.driver, "verify_row_count_failure")
        raise e

@when('Click the "Last Name" column header to sort in ascending order')
def step_sort_ascending(context):
    try:
        context.driver.find_element(By.XPATH, '//table[@id="table1"]/thead/tr/th[1]/span').click()
        time.sleep(2)
    except Exception as e:
        take_screenshot(context.driver, "sort_ascending_failure")
        raise e

@then('Verify the rows are sorted in ascending order by "Last Name"')
def step_verify_sort_ascending(context):
    try:
        sorted_last_names = [
            element.text.strip() for element in context.driver.find_elements(By.XPATH, '//table[@id="table1"]/tbody/tr/td[1]')
        ]
        assert sorted_last_names == sorted(sorted_last_names), f"Rows not in ascending order: {sorted_last_names}"
    except AssertionError as e:
        take_screenshot(context.driver, "verify_sort_ascending_failure")
        raise e

@when('Click the "Last Name" column header again to sort in descending order')
def step_sort_descending(context):
    try:
        context.driver.find_element(By.XPATH, '//table[@id="table1"]/thead/tr/th[1]/span').click()
        time.sleep(2)
    except Exception as e:
        take_screenshot(context.driver, "sort_descending_failure")
        raise e

@then('Verify the rows are sorted in descending order by "Last Name"')
def step_verify_sort_descending(context):
    try:
        sorted_last_names = [
            element.text.strip() for element in context.driver.find_elements(By.XPATH, '//table[@id="table1"]/tbody/tr/td[1]')
        ]
        assert sorted_last_names == sorted(sorted_last_names, reverse=True), f"Rows not in descending order: {sorted_last_names}"
    except AssertionError as e:
        take_screenshot(context.driver, "verify_sort_descending_failure")
        raise e

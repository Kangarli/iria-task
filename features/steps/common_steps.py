from behave import given
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def after_all(context):
    context.driver.quit()

@given('Navigate to "{url}"')
def step_open_browser(context, url):
    context.driver.get(url)

@given('I close the browser')
def step_close_browser(context):
    context.driver.quit()
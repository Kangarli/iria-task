from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def after_all(context):
    context.driver.quit()

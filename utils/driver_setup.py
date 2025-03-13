from selenium import webdriver

def setup_driver():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.maximize_window()
    return driver

def close_driver(driver):
    driver.quit()

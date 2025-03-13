import os
from datetime import datetime

def take_screenshot(driver, scenario_name):
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.mkdir(screenshots_dir)

    today = datetime.now().strftime("%Y-%m-%d")
    day_dir = os.path.join(screenshots_dir, today)
    if not os.path.exists(day_dir):
        os.mkdir(day_dir)

    timestamp = datetime.now().strftime("%H-%M-%S")
    screenshot_name = f"{scenario_name}_{timestamp}.png"
    filepath = os.path.join(day_dir, screenshot_name)

    driver.save_screenshot(filepath)

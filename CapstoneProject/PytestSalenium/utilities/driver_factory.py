from selenium import webdriver
from utilities.config_reader import get_browser


def get_driver():

    browser = get_browser().lower()

    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    return driver

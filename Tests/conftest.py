import time

from selenium import webdriver

def setup(browser):
    if browser.lower == 'chrome':
        driver = webdriver.Chrome()
        time.sleep(5)

    elif browser.lower == 'edge':
        driver = webdriver.Edge()

    else:
        driver = webdriver.Safari()
    return driver

setup("chrome")


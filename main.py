import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").is_displayed()

ProductText = driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
addToCartButton = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
clickCart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")

if ProductText=="Products":
    print(" Test has passed")
    assert True

else:
    print(" Test has Failed")
    assert False

time.sleep(5)

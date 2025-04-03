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

# Verify that the user is on the products page
ProductText = driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
if ProductText == "Products":
    print(" Test has passed")
    assert True
else:
    print(" Test has Failed")
    assert False

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

# Verify that cart is not empty
cartBadge = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span").text
if cartBadge and int(cartBadge) > 0:
    print("Test has passed: Cart is not empty")
    assert True
else:
    print("Test has failed: Cart is empty")
    assert False

#driver.find_element(By.XPATH, "//*[@id='cart_contents_container").is_displayed()
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Betty")
driver.find_element(By.ID, "last-name").send_keys("Malone")
driver.find_element(By.ID, "postal-code").send_keys("5598")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2").is_displayed()



# Verify that order has been processed.
CheckoutText = driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2").text
if CheckoutText == "Thank you for your order!":
    print(" Test has passed")
    assert True
else:
    print(" Test has Failed")
    assert False


time.sleep(10)



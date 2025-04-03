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
    print(" Test has passed: User is redirected to Products page")
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

# Verify that checkout Information fields are not leaving empty
firstName = driver.find_element(By.ID, "first-name").get_attribute("value")
lastName = driver.find_element(By.ID, "last-name").get_attribute("value")
postalCode = driver.find_element(By.ID, "postal-code").get_attribute("value")

if firstName and lastName and postalCode:
    print("Test has passed: Checkout information fields are not empty")
    assert True
else:
    print("Test has failed: Checkout information fields are empty")
    assert False

driver.find_element(By.ID, "continue").click()

# Verify that checkout overview page is displayed

CheckoutText = driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span").text
if CheckoutText == "Checkout: Overview":
    print("Test has passed: Checkout overview page is displayed")
    assert True
else:
    print("Test has failed: Checkout overview page is not displayed")
    assert False

# Verify that the item is displayed in the checkout overview page
itemName = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text
if itemName == "Sauce Labs Backpack":
    print("Test has passed: Item is displayed in the checkout overview page")
    assert True
else:
    print("Test has failed: Item is not displayed in the checkout overview page")
    assert False


# Verify that the item price is displayed in the checkout overview page
# itemPrice = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text
# if itemPrice == "$29.99":
#     print("Test has passed: Item price is displayed in the checkout overview page")
#     assert True
# else:
#     print("Test has failed: Item price is not displayed in the checkout overview page")
#     assert False

# Verify that the item quantity is displayed in the checkout overview page
# itemQuantity = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]").text
#
# if itemQuantity == "1":
#     print("Test has passed: Item quantity is displayed in the checkout overview page")
#     assert True
# else:
#     print("Test has failed: Item quantity is not displayed in the checkout overview page")
#     assert False

driver.find_element(By.ID, "finish").click()
driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2").is_displayed()

# Verify that order has been processed.
CheckoutText = driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2").text
if CheckoutText == "Thank you for your order!":
    print("Test has passed, Order has been processed")
    assert True
else:
    print(" Test has Failed")
    assert False


time.sleep(10)



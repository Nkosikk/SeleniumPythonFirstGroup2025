from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    productText_Xpath_id = "//*[@id='header_container']/div[2]/span"
    addToCart_Xpath_id = "//*[@id='add-to-cart-sauce-labs-backpack']"
    cartBadge_Xpath_id = "//*[@id='shopping_cart_container']/a/span"

    # add constructor
    def __init__(self, driver):
        self.driver = driver

    def verifyLandingPage(self, username):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.productText_Xpath_id)))
        element.isDisplayed()

    #add item to cart
    def clickAddToCartButton(self):
        element = self.driver.find_element(By.XPATH, self.addToCart_Xpath_id)
        element.click()

    #verify that item is added to cart
    def verifyItemAddedToCart(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.cartBadge_Xpath_id)))
        return element.is_displayed()




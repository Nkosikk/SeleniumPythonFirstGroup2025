from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    cartText_Xpath_id = "//*[@id='header_container']/div[2]/span"
    addToCart_Xpath_id = "//*[@id='add-to-cart-sauce-labs-backpack']"
    cartBadge_Xpath_id = "//*[@id='shopping_cart_container']/a/span"
    itemAddedToCart_Xpath_id = "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[1]"
    checkoutButton_id = "checkout"

    # add constructor
    def __init__(self, driver):
        self.driver = driver

    #verify cart page
    def verifyCartPage(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.cartText_Xpath_id)))
        element.isDisplayed()

    #verify that items are added to cart
    def verifyItemsInCart(self):
        element = self.driver.find_element(By.XPATH, self.itemAddedToCart_Xpath_id)
        element.is_displayed()

    #checkout cart
    def clickCheckoutButton(self):
        element = self.driver.find_element(By.ID, self.checkoutButton_id)
        element.click()



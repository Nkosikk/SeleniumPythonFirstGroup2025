from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage:
    title_ProductText_xpath = "//*[@id='header_container']/div[2]/span"
    button_addToCart_id = "add-to-cart-sauce-labs-backpack"
    button_cart_xpath = "//*[@id='shopping_cart_container']/a"

    def __init__(self, driver):
        self.driver = driver

    def verifyProductText(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.title_ProductText_xpath)))
        element.isDisplayed()

    def clickAddToCart(self):
     element = self.driver.find_element(By.ID, self.button_addToCart_id)
     element.click()

    def verifyAddToCart(self):
        element = self.driver.find_element(By.XPATH, self.button_cart_xpath)
        element.click()

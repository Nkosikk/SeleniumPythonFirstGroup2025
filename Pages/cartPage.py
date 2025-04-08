from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    #clicking cart
    title_CartText_xpath = "//span[@class='title'][contains(.,'Your Cart')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyCartTitle(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.title_CartText_xpath)))
        element.isDisplayed()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    checkoutText_Xpath_id = "//*[@id='header_container']/div[2]/span"
    textBox_firstname_id = "first-name"
    textBox_lastname_id = "last-name"
    textBox_zipcode_id = "first-name"
    button_continue_id = "continue"

    # add constructor
    def __init__(self, driver):
        self.driver = driver

    # verify checkout page

    def verifyCheckoutPage(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textCheckout_Xpath_id)))
        element.isDisplayed()

    def enterfirstName(self, firstname):
        wait = WebDriverWait(self.driver, 10)
        element = self.driver.find_element(By.ID, self.textBox_firstname_id)
        element.send_keys(firstname)

    def enterlastName(self, lastname):
        element = self.driver.find_element(By.ID, self.textBox_lastname_id)
        element.send_keys(lastname)

    def enterZipCode(self, zipcode):
            element = self.driver.find_element(By.ID, self.textBox_zipcode_id)
            element.send_keys(zipcode)

    def clickContinueButton(self):
        element = self.driver.find_element(By.ID, self.button_continue_id)
        element.click()

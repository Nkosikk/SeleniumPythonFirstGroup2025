from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ThankYouPage:
    textThankYouPage_Xpath_id = "//*[@id='checkout_complete_container']/h2"

    # add constructor
    def __init__(self, driver):
        self.driver = driver
    #verify thank you page

    def verifyThankYouPage(self, username):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textThankYouPage_Xpath_id)))
        element.isDisplayed()
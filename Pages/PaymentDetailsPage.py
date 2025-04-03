from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    checkoutOverviewText_Xpath_id = "//*[@id='header_container']/div[2]/span"
    referenceIDText = "//*[@id='checkout_summary_container']/div/div[2]/div[2]"
    finishButton_id = "finish"

    # add constructor
    def __init__(self, driver):
        self.driver = driver

    def verifyCheckoutOverviewLandingPage(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.checkoutOverviewText_Xpath_id)))
        element.isDisplayed()

    #verifyPaymentReference
    def paymentInformationRef(self):
        element = self.driver.find_element(By.XPATH, self.referenceIDText)
        element.isDisplayed()

    #Finshing the payment
    def clickFinishButton(self):
        element = self.driver.find_element(By.ID, self.finishButton_id)
        element.click()




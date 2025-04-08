from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OverviewPage:

    label_overview = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def verifyOverviewText(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.title_ProductText_xpath)))
        element.isDisplayed()

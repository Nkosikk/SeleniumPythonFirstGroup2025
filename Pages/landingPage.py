from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    title_ProductText_xpath = "//*[@id='header_container']/div[2]/span"

    def __init__(self, driver):
        self.driver = driver

    def verifyProductText(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.title_ProductText_xpath)))
        element.isDisplayed()

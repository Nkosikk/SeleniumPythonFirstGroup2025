from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textBox_username_id = "user-name"

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(EC.visibility_of_element_located((By.ID, self.textBox_username_id)))
        element.send_keys(username)


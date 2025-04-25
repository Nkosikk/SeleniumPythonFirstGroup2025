import time

import allure
import pytest
from selenium.webdriver.common.by import By

from Pages.landingPage import LandingPage
from Pages.loginPage import LoginPage
from Utils.readProperties_Login import ReadConfig_Login


class Test_SauceDemo:
    url = ReadConfig_Login().getUrl()
    username = ReadConfig_Login().getUserName()
    password = ReadConfig_Login().getPassword()

    def test_performlogin(self, setup):
        self.driver = setup
        self.login = LoginPage(self.driver)
        self.landingPage = LandingPage(self.driver)
        self.login.enterUsername(self.username)
        self.login.enterPassword(self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="login Page",
                      attachment_type=allure.attachment_type.PNG)
        self.login.clickLogin()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.order(2)
    @pytest.mark.success
    def test_verifySuccessfulloginToSauceDemo(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.landingPage = LandingPage(self.driver)
        self.login.enterUsername(self.username)
        self.login.enterPassword(self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="login Page",
                      attachment_type=allure.attachment_type.PNG)
        self.login.clickLogin()
        self.landingPage.verifyProductText()
        allure.attach(self.driver.get_screenshot_as_png(), name="Landing Page",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        self.driver.quit()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.order(1)
    @pytest.mark.unsuccessful
    def test_verifyUnSuccessfulloginToSauceDemo(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.enterUsername("invalid_user")  # Use invalid username
        self.login.enterPassword("invalid_password")  # Use invalid password
        allure.attach(self.driver.get_screenshot_as_png(), name="login error",
                      attachment_type=allure.attachment_type.PNG)
        self.login.clickLogin()

        # Verify error message is displayed
        error_message = self.driver.find_element(By.XPATH, "//*[@data-test='error']").text
        assert "Epic sadface" in error_message, "Error message not displayed for invalid login"

        allure.attach(self.driver.get_screenshot_as_png(), name="Error Message",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        self.driver.quit()







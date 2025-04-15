import time

import allure
import pytest

from Pages.loginPage import LoginPage
from Utils.readProperties_Login import ReadConfig_Login


class Test_SauceDemo:
    url = ReadConfig_Login().getUrl()
    username = ReadConfig_Login().getUserName()
    password = ReadConfig_Login().getPassword()


    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_loginToSauceDemo(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.login=LoginPage(self.driver)
        self.login.enterUsername(self.username)


        allure.attach(self.driver.get_screenshot_as_png(), name="login Page", attachment_type=allure.attachment_type.PNG)


        time.sleep(2)







        self.driver.quit()

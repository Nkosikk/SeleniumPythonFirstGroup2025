import allure
import pytest

from Pages.landingPage import LandingPage
from Pages.loginPage import LoginPage
from tests import test_Login
from Utils.readProperties_Login import ReadConfig_Login


class tests_landingpage:
    url = ReadConfig_Login().getUrl()
    username = ReadConfig_Login().getUserName()
    password = ReadConfig_Login().getPassword()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    @pytest.mark.order(3)
    @pytest.mark.addtocart
    def test_verifyItemAddetoCart(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        test_Login.Test_SauceDemo().test_performlogin(self.driver)
        self.landingPage = LandingPage(self.driver)
        self.landingPage.verifyProductText()
        self.landingPage.clickAddToCart()
        allure.attach(self.driver.get_screenshot_as_png(), name="Landing Page",
                      attachment_type=allure.attachment_type.PNG)

        self.driver.quit()

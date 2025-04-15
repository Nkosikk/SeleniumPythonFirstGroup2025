import pytest

from Utils.readProperties_Login import ReadConfig_Login


class Test_SauceDemo:
    url = ReadConfig_Login().getUrl()
    username = ReadConfig_Login().getUserName()
    password = ReadConfig_Login().getPassword()

    @pytest.mark.sanity
    def test_loginToSauceDemo(self, setup):
        self.driver = setup
        self.driver.get(self.url)

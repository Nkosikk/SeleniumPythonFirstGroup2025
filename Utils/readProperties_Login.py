import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/Login.ini")


class ReadConfig_Login():

    @staticmethod
    def geturl():
        return config.get("Common Details", "url")

    @staticmethod
    def getuserName():
        return config.get("Login Details", "username")

    @staticmethod
    def getpassWord():
        return config.get("Login Details", "password")
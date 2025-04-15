import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/Login.ini")


class ReadConfig_Login():

    @staticmethod
    def getUrl():
        return config.get("Common Details", "url")

    @staticmethod
    def getUserName():
        return config.get("Login Details", "username")

    @staticmethod
    def getPassword():
        return config.get("Login Details", "password")
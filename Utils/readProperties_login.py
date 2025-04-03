import configparser

config = configparser.RawConfigParser()
config.read(".Configurations/Login.ini")

class ReadConfig_Log():
    @staticmethod
    def getURL():
        return config.get("Common Details", "url")

    @staticmethod
    def getUserName():
        return config.get("Login Details", "url")

    @staticmethod
    def getLastName():
        return config.get("Login Details", "url")
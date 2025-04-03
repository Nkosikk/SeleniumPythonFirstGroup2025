import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/Login.ini")

class ReadConfig_Login():


    @staticmethod
    def getUrl(self):
        return config.get("Common Details","url")


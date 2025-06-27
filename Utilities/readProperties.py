import configparser


config=configparser.ConfigParser(interpolation=None)
config.read(".\\Configurations\\config.ini")

class readConfig():
    @staticmethod
    def getURL():
        url=config.get("main", 'baseURL')
        return url;

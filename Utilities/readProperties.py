import os
import configparser

class readConfig:
    @staticmethod
    def getURL():
        config = configparser.ConfigParser(interpolation=None)
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "..", "Configurations", "config.ini")
        config.read(config_path)

        return config.get("main", "baseURL")
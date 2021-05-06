import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod  # makes class and method declare w/o parameter (self)
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        useremail = config.get('common info', 'username')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password


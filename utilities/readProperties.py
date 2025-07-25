import configparser
import time
from selenium import webdriver

# from testCases.conftest import initialize_browser
from utilities.customeLogger import LogGen

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common data', 'Username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'Password')
        return password

















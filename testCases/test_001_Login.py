import time
import os

from jinja2.nodes import Import



import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from utilities import ExcelUtils
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen
from utilities.reusableMethods import page_URL_Verification


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.join(os.getcwd(), "TestData", "Kirthi_TestData.xlsx")

    def open_app(self, driver):
        """Reusable method to launch app and maximize window"""
        driver.get(self.baseURL)
        driver.maximize_window()

    def test_login1(self, initialize_browser):
        self.logger.info("**Test_001_Login - Verifying Login Page URL**")
        self.driver = initialize_browser
        self.open_app(self.driver)

        verifier = page_URL_Verification(self.driver, self.logger)
        verifier.verify_url(
            expected_text="login",
            screenshot_path_pass="./Screenshots/LogInPage/LoginPageURL_Pass.png",
            screenshot_path_fail="./Screenshots/LogInPage/LoginPageURL_FAIL.png"
        )

    def test_login2(self, initialize_browser):
        self.logger.info("**Test_001_Login - Verifying LOGIN with Multiple Users**")
        self.driver = initialize_browser
        self.open_app(self.driver)

        rows = ExcelUtils.getRowCount(self.path, 'login')
        # Testing 

        for r in range(2, rows + 1):
            username = ExcelUtils.readData(self.path, 'login', r, 1)
            password = ExcelUtils.readData(self.path, 'login', r, 2)

            login_page = LoginPage(self.driver)
            login_page.login(username,password)
            time.sleep(5)  # Optional: Replace with WebDriverWait if needed

        verifier = page_URL_Verification(self.driver, self.logger)
        verifier.verify_url(
            expected_text="home",
            screenshot_path_pass="./Screenshots/LogInPage/HomeURL_Pass.png",
            screenshot_path_fail="./Screenshots/LogInPage/HomeURL_FAIL.png"
        )

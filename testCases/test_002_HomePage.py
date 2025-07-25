import time
import os
from pageObjects.LoginPage import LoginPage
from utilities import ExcelUtils
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.reusableMethods import page_URL_Verification


class Test_002_Homepage:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.join(os.getcwd(), "TestData", "Kirthi_TestData.xlsx")

    def open_application(self, driver):
        driver.get(self.baseURL)
        driver.maximize_window()

    def test_Homepage(self, initialize_browser):
        self.logger.info("**Test_002_Homepage - Verifying Home Page after Login**")
        driver = initialize_browser
        self.open_application(driver)

        username = ExcelUtils.readData(self.path, 'login', 5, 1)
        password = ExcelUtils.readData(self.path, 'login', 5, 2)

        login_page = LoginPage(driver)
        login_page.login(username, password)
        time.sleep(5)  # Optional: Replace with WebDriverWait if needed

        verifier = page_URL_Verification(driver, self.logger)
        verifier.verify_url(
            expected_text="home",
            screenshot_path_pass="./Screenshots/HomePage/HomeURL_Pass.png",
            screenshot_path_fail="./Screenshots/HomePage/HomeURL_FAIL.png"
        )

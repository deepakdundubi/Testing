import time
import os
from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Master import Master
from pageObjects.ProductMaster import ProductMaster
from utilities import ExcelUtils
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.reusableMethods import page_URL_Verification
from utilities.reusableMethods import GenericUtils
from utilities.reusableMethods import StaticDropdown


class Test_009_ProductMaster:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.join(os.getcwd(), "TestData", "Kirthi_TestData.xlsx")

    def login_and_navigate_to_productMaster(self, driver):
        driver.get(self.baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        username = ExcelUtils.readData(self.path, 'login', 5, 1)
        password = ExcelUtils.readData(self.path, 'login', 5, 2)

        login_page = LoginPage(driver)
        login_page.login(username, password)
        time.sleep(2)
        home_page = HomePage(driver)
        home_page.navigateToMasterMenu()
        master_page = Master(driver)
        master_page.goToProductMasterSection()
        time.sleep(2)

        verifier = page_URL_Verification(driver, self.logger)
        verifier.verify_url(
            expected_text="product",
            screenshot_path_pass="./Screenshots/ProductMaster/ProductURL_Pass.png",
            screenshot_path_fail="./Screenshots/ProductMaster/ProductURL_FAIL.png"
        )

    def test_ProductMaster(self, initialize_browser):
        driver = initialize_browser
        self.logger.info("**Test_008_Employee - Start**")
        self.login_and_navigate_to_productMaster(driver)

        productMaster_page = ProductMaster(driver)
        productMaster_page.ClickOnNew()

        productMaster_page.ProductType(ExcelUtils.readData(self.path, 'product', 3, 2))
        time.sleep(10)












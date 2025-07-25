import time
from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Master import Master
from pageObjects.Unitmaster import UnitMaster
from utilities import ExcelUtils
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.reusableMethods import page_URL_Verification


class Test_003_UnitMaster:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = "C:\\Users\\dell\\PycharmProjects\\Autotronics01\\pythonProject\\TestData\\Kirthi_TestData.xlsx"

    def login_and_navigate_to_unit(self, driver):
        driver.get(self.baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Login
        username = ExcelUtils.readData(self.path, 'login', 5, 1)
        password = ExcelUtils.readData(self.path, 'login', 5, 2)

        login_page = LoginPage(driver)
        login_page.login(username, password)
        time.sleep(2)

        home_page = HomePage(driver)
        home_page.navigateToMasterMenu()

        master_page = Master(driver)
        master_page.goToUnitSection()
        time.sleep(2)

        # Verify URL contains 'Unitmaster'
        verifier = page_URL_Verification(driver, self.logger)
        verifier.verify_url(
            expected_text="unit",
            screenshot_path_pass="./Screenshots/UnitMaster/UnitMasterURL_Pass.png",
            screenshot_path_fail="./Screenshots/UnitMaster/UnitMasterURL_FAIL.png"
        )

    def test_Uit(self, initialize_browser):
        driver = initialize_browser
        self.logger.info("**Test_007_UnitMaster - Start**")

        self.login_and_navigate_to_unit(driver)
        unitmaster_page = UnitMaster(driver)

        # Create New Unit master
        unit_name = ExcelUtils.readData(self.path, 'unit', 2, 2)
        unitmaster_page.ClickOnNew()
        time.sleep(1)
        unitmaster_page.EnterUnit(unit_name)
        unitmaster_page.ClickOnSave()
        time.sleep(2)
        driver.save_screenshot("./Screenshots/UnitMaster/2_New_UnitMaster.png")
        self.logger.info("***** NEW UnitMaster CREATED *****")

        # Search and Edit Category
        search_term = ExcelUtils.readData(self.path, 'unit', 5, 2)
        unitmaster_page.SearchField(search_term)
        self.logger.info("* Search UnitMaster displayed *")
        time.sleep(1)
        unitmaster_page.ClickOnEdit()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/UnitMaster/3_Edit_UnitMaster.png")

        # Update Category Name
        updated_name = ExcelUtils.readData(self.path, 'unit', 8, 2)
        unitmaster_page.UpdateUnit(updated_name)
        time.sleep(1)
        unitmaster_page.ClickOnUpdate()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/UnitMaster/4_Update_UnitMaster.png")
        self.logger.info("*** UPDATED UnitMaster SUCCESSFULLY ***")

        # # Optionally: Delete Category
        # delete_name = ExcelUtils.readData(self.path, 'unit', 11, 2)
        # unitmaster_page.SearchField(delete_name)
        # time.sleep(2)
        # unitmaster_page.DeleteUnit()
        # driver.save_screenshot("./Screenshots/UnitMaster/5_Delete_UnitMaster.png")
        # unitmaster_page.DeleteConfirm()
        # time.sleep(2)

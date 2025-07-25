import time
from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Master import Master
from pageObjects.Designation import Designation
from utilities import ExcelUtils
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.reusableMethods import page_URL_Verification


class Test_007_Designation:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = "C:\\Users\\dell\\PycharmProjects\\Autotronics01\\pythonProject\\TestData\\Kirthi_TestData.xlsx"

    def login_and_navigate_to_designation(self, driver):
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
        master_page.goToDesignation()
        time.sleep(2)

        # Verify URL contains 'Designation'
        verifier = page_URL_Verification(driver, self.logger)
        verifier.verify_url(
            expected_text="designation",
            screenshot_path_pass="./Screenshots/Designation/DesignationURL_Pass.png",
            screenshot_path_fail="./Screenshots/Designation/DesignationURL_FAIL.png"
        )

    def test_Department(self, initialize_browser):
        driver = initialize_browser
        self.logger.info("**Test_006_Designation - Start**")

        self.login_and_navigate_to_designation(driver)
        designation_page = Designation(driver)

        # Create New Department
        category_name = ExcelUtils.readData(self.path, 'designation', 2, 2)
        designation_page.ClickOnNew()
        time.sleep(1)
        designation_page.EnterDesignationName(category_name)
        designation_page.ClickOnSave()
        time.sleep(2)
        driver.save_screenshot("./Screenshots/Designation/2_New_Designation.png")
        self.logger.info("***** NEW Designation CREATED *****")

        # Search and Edit Designation
        search_term = ExcelUtils.readData(self.path, 'designation', 5, 2)
        designation_page.SearchField(search_term)
        self.logger.info("* Search Designation displayed *")
        time.sleep(1)
        designation_page.ClickOnEdit()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/Designation/3_Edit_Designation.png")

        # Update Designation Name
        updated_name = ExcelUtils.readData(self.path, 'designation', 8, 2)
        designation_page.UpdateDesignationName_Field(updated_name)
        time.sleep(1)
        designation_page.ClickOnUpdate()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/Designation/4_Update_Designation.png")
        self.logger.info("*** UPDATED Designation SUCCESSFULLY ***")

        # # Optionally: Delete Designation
        # delete_name = ExcelUtils.readData(self.path, 'designation', 11, 2)
        # designation_page.SearchField(delete_name)
        # time.sleep(2)
        # designation_page.DeleteDesignation()
        # driver.save_screenshot("./Screenshots/Designation/5_Delete_Designation.png")
        # designation_page.DeleteConfirm()
        # time.sleep(2)

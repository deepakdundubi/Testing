import time
import os
from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Master import Master
from pageObjects.SubCategory import SubCategory
from utilities import ExcelUtils
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.reusableMethods import page_URL_Verification
from utilities.reusableMethods import GenericUtils


class Test_005_SubCategory:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.join(os.getcwd(), "TestData", "Kirthi_TestData.xlsx")

    def login_and_navigate_to_subcategory(self, driver):
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
        master_page.goToSubCategorySection()
        time.sleep(2)

        verifier = page_URL_Verification(driver, self.logger)
        verifier.verify_url(
            expected_text="sub-category",
            screenshot_path_pass="./Screenshots/SubCategory/SubCategoryURL_Pass.png",
            screenshot_path_fail="./Screenshots/SubCategory/SubCategoryURL_FAIL.png"
        )

    def test_SubCategory(self, initialize_browser):
        driver = initialize_browser
        self.logger.info("**Test_004_SubCategory - Start**")
        self.login_and_navigate_to_subcategory(driver)

        subcategory_page = SubCategory(driver)
##Part of code need to paste for dropdown present below
##Calling Dropdown Functionality from Reusable method page
        subcategory_page.ClickOnNew()
        GenericUtils.select_value_from_custom_dropdown(
            click_dropdown_fn=subcategory_page.ClickOnCategoryDropdown,
            search_value_fn=subcategory_page.SearCategoryInDropdown,
            click_result_fn=subcategory_page.ClickOnCategoryValue,
            value_to_select=ExcelUtils.readData(self.path, 'subcategory', 2, 2),
            logger=self.logger,
            driver=driver,
            screenshot_path="./Screenshots/SubCategory/DropdownSelected.png"
        )
        subcategory_name = ExcelUtils.readData(self.path, 'subcategory', 5, 2)
        subcategory_page.EnterSubCategoryName(subcategory_name)
        subcategory_page.ClickOnSave()
        driver.save_screenshot("./Screenshots/SubCategory/3_New_SubCategory.png")
        self.logger.info("***** NEW SUB-CATEGORY CREATED *****")
        time.sleep(2)

        # Edit SubCategory
        search_term = ExcelUtils.readData(self.path, 'subcategory', 8, 2)
        subcategory_page.SearchSubCategory(search_term)
        self.logger.info("*Search Sub-Category displayed*")
        time.sleep(1)
        subcategory_page.ClickOnEdit()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/SubCategory/4_Edit_Sub_Category.png")

        # Update SubCategory
        updated_name = ExcelUtils.readData(self.path, 'subcategory', 11, 2)
        subcategory_page.UpdateSubCategoryName_Field(updated_name)
        time.sleep(1)
        subcategory_page.ClickOnUpdate()
        driver.save_screenshot("./Screenshots/SubCategory/5_Update_SubCategory.png")
        self.logger.info("*** UPDATED SUB-CATEGORY SUCCESSFULLY ***")
        time.sleep(2)

        # # Delete SubCategory
        # delete_name = ExcelUtils.readData(self.path, 'subcategory', 14, 2)
        # subcategory_page.SearchSubCategory(delete_name)
        # time.sleep(1)
        # subcategory_page.DeleteSubCategory()
        # time.sleep(1)
        # subcategory_page.DeleteConfirm()
        # driver.save_screenshot("./Screenshots/SubCategory/6_Delete_SubCategory.png")
        # time.sleep(1)



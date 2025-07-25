import time
from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Master import Master
from pageObjects.Category import Category
from utilities import ExcelUtils
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.reusableMethods import page_URL_Verification


class Test_004_Category:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = "C:\\Users\\dell\\PycharmProjects\\Autotronics01\\pythonProject\\TestData\\Kirthi_TestData.xlsx"

    def login_and_navigate_to_category(self, driver):
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
        master_page.goToCategorySection()
        time.sleep(2)

        # Verify URL contains 'category'
        verifier = page_URL_Verification(driver, self.logger)
        verifier.verify_url(
            expected_text="category",
            screenshot_path_pass="./Screenshots/Category/CategoryURL_Pass.png",
            screenshot_path_fail="./Screenshots/Category/CategoryURL_FAIL.png"
        )

    def test_Category(self, initialize_browser):
        driver = initialize_browser
        self.logger.info("**Test_003_Category - Start**")

        self.login_and_navigate_to_category(driver)
        category_page = Category(driver)

        # Create New Category
        category_name = ExcelUtils.readData(self.path, 'category', 2, 2)
        category_page.ClickOnNew()
        time.sleep(1)
        category_page.EnterCategoryName(category_name)
        category_page.ClickOnSave()
        time.sleep(2)
        driver.save_screenshot("./Screenshots/Category/2_New_Category.png")
        self.logger.info("***** NEW PRODUCT CATEGORY CREATED *****")

        # Search and Edit Category
        search_term = ExcelUtils.readData(self.path, 'category', 5, 2)
        category_page.SearchField(search_term)
        self.logger.info("* Search Category displayed *")
        time.sleep(1)
        category_page.ClickOnEdit()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/Category/3_Edit_Category.png")

        # Update Category Name
        updated_name = ExcelUtils.readData(self.path, 'category', 8, 2)
        category_page.UpdateCategoryName_Field(updated_name)
        time.sleep(1)
        category_page.ClickOnUpdate()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/Category/4_Update_Category.png")
        self.logger.info("*** UPDATED PRODUCT CATEGORY SUCCESSFULLY ***")

        # # Optionally: Delete Category
        # delete_name = ExcelUtils.readData(self.path, 'category', 11, 2)
        # category_page.SearchField(delete_name)
        # time.sleep(2)
        # category_page.DeleteCategory()
        # driver.save_screenshot("./Screenshots/Category/5_DeleteProduct_Category.png")
        # category_page.DeleteConfirm()
        # time.sleep(2)

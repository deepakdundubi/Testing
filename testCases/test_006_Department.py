import time
from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Master import Master
from pageObjects.Department import Department
from utilities import ExcelUtils
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.reusableMethods import page_URL_Verification


class Test_006_Department:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = "C:\\Users\\dell\\PycharmProjects\\Autotronics01\\pythonProject\\TestData\\Kirthi_TestData.xlsx"

    def login_and_navigate_to_department(self, driver):
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
        master_page.goToDepartment()
        time.sleep(2)

        # Verify URL contains 'Department'
        verifier = page_URL_Verification(driver, self.logger)
        verifier.verify_url(
            expected_text="department",
            screenshot_path_pass="./Screenshots/Department/DepartmentURL_Pass.png",
            screenshot_path_fail="./Screenshots/Department/DepartmentURL_FAIL.png"
        )

    def test_Department(self, initialize_browser):
        driver = initialize_browser
        self.logger.info("**Test_005_Department - Start**")

        self.login_and_navigate_to_department(driver)
        department_page = Department(driver)

        # Create New Department
        department_name = ExcelUtils.readData(self.path, 'department', 2, 2)
        department_page.ClickOnNew()
        time.sleep(1)
        department_page.EnterDepartmentName(department_name)
        department_page.ClickOnSave()
        time.sleep(2)
        driver.save_screenshot("./Screenshots/Department/2_New_Department.png")
        self.logger.info("***** NEW Department CREATED *****")

        # Search and Edit Category
        search_term = ExcelUtils.readData(self.path, 'department', 5, 2)
        department_page.SearchField(search_term)
        self.logger.info("* Search Department displayed *")
        time.sleep(1)
        department_page.ClickOnEdit()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/Department/3_Edit_Department.png")

        # Update Category Name
        updated_name = ExcelUtils.readData(self.path, 'department', 8, 2)
        department_page.UpdateDepartmentName_Field(updated_name)
        time.sleep(1)
        department_page.ClickOnUpdate()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/Department/4_Update_Department.png")
        self.logger.info("*** UPDATED DEPARTMENT SUCCESSFULLY ***")

        # # Optionally: Delete Category
        # delete_name = ExcelUtils.readData(self.path, 'department', 11, 2)
        # department_page.SearchField(delete_name)
        # time.sleep(2)
        # department_page.DeleteDepartment()
        # driver.save_screenshot("./Screenshots/Department/5_Delete_Department.png")
        # department_page.DeleteConfirm()
        # time.sleep(2)

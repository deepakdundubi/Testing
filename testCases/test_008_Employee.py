import time
import os
from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Master import Master
from pageObjects.Employee import Employee
from utilities import ExcelUtils
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.reusableMethods import page_URL_Verification
from utilities.reusableMethods import GenericUtils


class Test_008_Employee:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.join(os.getcwd(), "TestData", "Kirthi_TestData.xlsx")

    def login_and_navigate_to_employee(self, driver):
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
        master_page.goToEmployeeSection()
        time.sleep(2)

        verifier = page_URL_Verification(driver, self.logger)
        verifier.verify_url(
            expected_text="employee",
            screenshot_path_pass="./Screenshots/Employee/EmployeeURL_Pass.png",
            screenshot_path_fail="./Screenshots/Employee/EmployeeURL_FAIL.png"
        )

    def test_Employee(self, initialize_browser):
        driver = initialize_browser
        self.logger.info("**Test_008_Employee - Start**")
        self.login_and_navigate_to_employee(driver)

        employee_page = Employee(driver)
        employee_page.ClickOnNew()

        employee_name = ExcelUtils.readData(self.path, 'employee', 2, 2)
        employee_page.EnterEmployeeName(employee_name)

        email = ExcelUtils.readData(self.path, 'employee', 5, 2)
        employee_page.EnterEmail(email)

        phoneNo = ExcelUtils.readData(self.path, 'employee', 8, 2)
        employee_page.EnterPhoneNo(phoneNo)

        #Department
        GenericUtils.select_value_from_custom_dropdown(
            click_dropdown_fn=employee_page.ClickOnDepartmentDropdown,
            search_value_fn=employee_page.SearchDepartment,
            click_result_fn=employee_page.SelectDepartment,
            value_to_select=ExcelUtils.readData(self.path, 'employee', 11, 2),
            logger=self.logger,
            driver=driver,
            screenshot_path="./Screenshots/Employee/DepartmentSelected.png"
        )
        #Designation
        GenericUtils.select_value_from_custom_dropdown(
            click_dropdown_fn=employee_page.ClickOnDesignationDropdown,
            search_value_fn=employee_page.SearchDesignation,
            click_result_fn=employee_page.SelectDesignation,
            value_to_select=ExcelUtils.readData(self.path, 'employee', 14, 2),
            logger=self.logger,
            driver=driver,
            screenshot_path="./Screenshots/Employee/DesignationSelected.png"
        )
        #First Reporting Authority
        GenericUtils.select_value_from_custom_dropdown(
            click_dropdown_fn=employee_page.ClickOn1stReportingDropdown,
            search_value_fn=employee_page.Search1stReporting,
            click_result_fn=employee_page.Select1stReporting,
            value_to_select=ExcelUtils.readData(self.path, 'employee', 17, 2),
            logger=self.logger,
            driver=driver,
            screenshot_path="./Screenshots/Employee/1stReportingSelected.png"
        )
        #Second Report Authority
        GenericUtils.select_value_from_custom_dropdown(
            click_dropdown_fn=employee_page.ClickOn2ndReportingDropdown,
            search_value_fn=employee_page.Search2ndReporting,
            click_result_fn=employee_page.Select2ndReporting,
            value_to_select=ExcelUtils.readData(self.path, 'employee', 20, 2),
            logger=self.logger,
            driver=driver,
            screenshot_path="./Screenshots/Employee/2ndReportingSelected.png"
        )
        time.sleep(2)
        employee_page.ClickOnSystemUser()

        #System Access Group
        GenericUtils.select_value_from_custom_dropdown(
            click_dropdown_fn=employee_page.ClickOnSystemAccessGroupDropdown,
            search_value_fn=employee_page.SearchAccessGroup,
            click_result_fn=employee_page.SelectAccessGroup,
            value_to_select=ExcelUtils.readData(self.path, 'employee', 23, 2),
            logger=self.logger,
            driver=driver,
            screenshot_path="./Screenshots/Employee/2ndReportingSelected.png"
        )

        password = ExcelUtils.readData(self.path, 'employee', 26, 2)
        employee_page.EnterPassword(password)

        employee_page.ClickOnSave()
        time.sleep(10)

        # Search and Edit Designation
        search_term = ExcelUtils.readData(self.path, 'employee', 2, 5)
        employee_page.SearchField(search_term)
        self.logger.info("* Search Employee displayed *")
        time.sleep(1)
        employee_page.ClickOnEdit()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/Designation/3_Edit_Designation.png")

        # Update Employee Name
        updated_name = ExcelUtils.readData(self.path, 'employee', 5, 5)
        employee_page.UpdateEmployeeName_Field(updated_name)
        time.sleep(1)
        employee_page.ClickOnUpdate()
        time.sleep(1)
        driver.save_screenshot("./Screenshots/Employee/4_Update_Employee.png")
        self.logger.info("*** UPDATED Designation SUCCESSFULLY ***")

        # # Optionally: Delete Employee
        # delete_name = ExcelUtils.readData(self.path, 'employee', 8, 5)
        # employee_page.SearchField(delete_name)
        # time.sleep(2)
        # employee_page.DeleteEmployee()
        # driver.save_screenshot("./Screenshots/Employee/5_Delete_Employee.png")
        # employee_page.DeleteConfirm()
        # time.sleep(2)


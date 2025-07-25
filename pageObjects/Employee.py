from selenium.webdriver.common.by import By


class Employee:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

    def EnterEmployeeName(self,Employee_name):
        self.driver.find_element(By.XPATH,"//input[@id='employee_name']").send_keys(Employee_name)

    def EnterEmail(self,Email):
        self.driver.find_element(By.XPATH,"//input[@id='email']").send_keys(Email)

    def EnterPhoneNo(self,Phone_No):
        self.driver.find_element(By.XPATH,"//input[@id='phone_no']").send_keys(Phone_No)

    def ClickOnNew(self):
        self.driver.find_element(By.XPATH, '//span[text()="+ Add New"]').click()

    def ClickOnDepartmentDropdown(self):
        self.driver.find_element(By.XPATH,"//span[text()='Select Department']").click()

    def SearchDepartment(self, Department):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(Department)

    def SelectDesignation(self):
        self.driver.find_element(By.XPATH,"//div[@class='p-element elipsis']").click()

    def ClickOnDesignationDropdown(self):
        self.driver.find_element(By.XPATH,"//span[text()='Select Designation']").click()

    def SearchDesignation(self, Designation):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(Designation)

    def SelectDepartment(self):
        self.driver.find_element(By.XPATH,"//div[@class='p-element elipsis']").click()

    def ClickOn1stReportingDropdown(self):
        self.driver.find_element(By.XPATH,"//span[text()='Select First Reporting Authority']").click()

    def Search1stReporting(self, FirstReporting):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(FirstReporting)

    def Select1stReporting(self):
        self.driver.find_element(By.XPATH,"(//div[@class='p-element elipsis'])[1]").click()

    def ClickOn2ndReportingDropdown(self):
        self.driver.find_element(By.XPATH,"//span[text()='Select Second Report Authority']").click()

    def Search2ndReporting(self, SecondReporting):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(SecondReporting)

    def Select2ndReporting(self):
        self.driver.find_element(By.XPATH,"(//div[@class='p-element elipsis'])[1]").click()

    def ClickOnSystemUser(self):
        self.driver.find_element(By.XPATH,"//span[@class='p-inputswitch-slider']").click()

    def ClickOnSystemAccessGroupDropdown(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Select System Access Group')]").click()

    def SearchAccessGroup(self,AccessGroup):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(AccessGroup)

    def SelectAccessGroup(self):
        self.driver.find_element(By.XPATH,"(//div[@class='p-element elipsis'])[1]").click()

    def EnterPassword(self,Password):
        self.driver.find_element(By.XPATH,"//input[@id='user_password']").send_keys(Password)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def ClickOnEdit(self):
        self.driver.find_element(By.XPATH, '//span[@class="p-button-icon pi pi-pen-to-square"]').click()

    def SearchField(self, Employee_Name):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').clear()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').send_keys(Employee_Name)

    def UpdateEmployeeName_Field(self, Update_employee_name):
        self.driver.find_element(By.XPATH, "//input[@id='employee_name']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='employee_name']").send_keys(Update_employee_name)

    def ClickOnUpdate(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def DeleteEmployee(self):
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-trash']").click()

    def DeleteConfirm(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Yes')]").click()



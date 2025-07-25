from selenium.webdriver.common.by import By


class Department:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

    def ClickOnNew(self):
        self.driver.find_element(By.XPATH, '//span[text()="+ Add New"]').click()

    def EnterDepartmentName(self, department_name):
        self.driver.find_element(By.XPATH, "//input[@id='department_name']").send_keys(department_name)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def SearchField(self, department_Name):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').clear()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').send_keys(department_Name)


    def ClickOnEdit(self):
        self.driver.find_element(By.XPATH, '//span[@class="p-button-icon pi pi-pen-to-square"]').click()

    def UpdateDepartmentName_Field(self, Update_department_name):
        self.driver.find_element(By.XPATH, "//input[@id='department_name']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='department_name']").send_keys(Update_department_name)

    def ClickOnUpdate(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def DeleteDepartment(self):
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-trash']").click()

    def DeleteConfirm(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Yes')]").click()

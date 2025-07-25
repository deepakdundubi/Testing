from selenium.webdriver.common.by import By


class Designation:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

    def ClickOnNew(self):
        self.driver.find_element(By.XPATH, '//span[text()="+ Add New"]').click()

    def EnterDesignationName(self, designation_name):
        self.driver.find_element(By.XPATH, "//input[@id='designation_name']").send_keys(designation_name)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def SearchField(self, designation_Name):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').clear()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').send_keys(designation_Name)


    def ClickOnEdit(self):
        self.driver.find_element(By.XPATH, '//span[@class="p-button-icon pi pi-pen-to-square"]').click()

    def UpdateDesignationName_Field(self, Update_designation_name):
        self.driver.find_element(By.XPATH, "//input[@id='designation_name']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='designation_name']").send_keys(Update_designation_name)

    def ClickOnUpdate(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def DeleteDesignation(self):
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-trash']").click()

    def DeleteConfirm(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Yes')]").click()

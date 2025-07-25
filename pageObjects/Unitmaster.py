from selenium.webdriver.common.by import By


class UnitMaster:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

    def ClickOnNew(self):
        self.driver.find_element(By.XPATH, '//span[text()="+ Add New"]').click()

    def EnterUnit(self, unit):
        self.driver.find_element(By.XPATH, "//input[@id='unit']").send_keys(unit)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def SearchField(self, unit):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').clear()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').send_keys(unit)


    def ClickOnEdit(self):
        self.driver.find_element(By.XPATH, '//span[@class="p-button-icon pi pi-pen-to-square"]').click()

    def UpdateUnit(self, Update_Unit):
        self.driver.find_element(By.XPATH, "//input[@id='unit']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='unit']").send_keys(Update_Unit)

    def ClickOnUpdate(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def DeleteUnit(self):
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-trash']").click()

    def DeleteConfirm(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Yes')]").click()

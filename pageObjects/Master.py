from selenium.webdriver.common.by import By


class Master:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver
    # ACTION METHODS

    def ClickUnitMaster(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Unit Master')]").click()
    def goToUnitSection(self):
        self.ClickUnitMaster()

    def ClickCategoryMaster(self):
        self.driver.find_element(By.XPATH,"//span[text()='Category Master']").click()
    def goToCategorySection(self):
        self.ClickCategoryMaster()

    def ClickSubCategory(self):
        self.driver.find_element(By.XPATH,"//span[text()='Sub Category Master']").click()
    def goToSubCategorySection(self):
        self.ClickSubCategory()

    def ClickDepartment(self):
        self.driver.find_element(By.XPATH,"//span[text()='Department']").click()
    def goToDepartment(self):
        self.ClickDepartment()

    def ClickDesignation(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Designation')]").click()
    def goToDesignation(self):
        self.ClickDesignation()

    def ClickEmployee(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Employee')]").click()
    def goToEmployeeSection(self):
        self.ClickEmployee()

    def ClickHolidayMaster(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Holiday Master')]").click()

    def ClickProductMaster(self):
        self.driver.find_element(By.XPATH,"//span[text()='Product Master']").click()
    def goToProductMasterSection(self):
        self.ClickProductMaster()

    def ClickPartyMaster(self):
        self.driver.find_element(By.XPATH,"//span[text()='Party Master']").click()
    def goToPartyMasterSection(self):
        self.ClickPartyMaster()

    def ClickTermsCondition(self):
        self.driver.find_element(By.XPATH,"//span[text()='Terms And Conditions']").click()

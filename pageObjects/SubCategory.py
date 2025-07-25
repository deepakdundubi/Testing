from selenium.webdriver.common.by import By


class SubCategory:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

    def ClickOnNew(self):
        self.driver.find_element(By.XPATH, '//span[text()="+ Add New"]').click()

    def ClickOnCategoryDropdown(self):
        self.driver.find_element(By.XPATH,"//span[text()='Select Category']").click()


    def SearCategoryInDropdown(self, Category):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(Category)

    def ClickOnCategoryValue(self):
        self.driver.find_element(By.XPATH,"//div[@class='p-element elipsis']").click()

    def EnterSubCategoryName(self, Subcategory_name):
        self.driver.find_element(By.XPATH, "//input[@id='sub_category_name']").send_keys(Subcategory_name)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def SearchSubCategory(self, category_Name):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').clear()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').send_keys(category_Name)


    def ClickOnEdit(self):
        self.driver.find_element(By.XPATH, '//span[@class="p-button-icon pi pi-pen-to-square"]').click()

    def UpdateSubCategoryName_Field(self, Update_Subcategory_name):
        self.driver.find_element(By.XPATH, "//input[@id='sub_category_name']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='sub_category_name']").send_keys(Update_Subcategory_name)

    def ClickOnUpdate(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def DeleteSubCategory(self):
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-trash']").click()

    def DeleteConfirm(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Yes')]").click()

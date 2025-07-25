from selenium.webdriver.common.by import By


class Category:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

    def ClickOnNew(self):
        self.driver.find_element(By.XPATH, '//span[text()="+ Add New"]').click()

    def EnterCategoryName(self, category_name):
        self.driver.find_element(By.XPATH, "//input[@id='category_name']").send_keys(category_name)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def SearchField(self, category_Name):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').clear()
        self.driver.find_element(By.XPATH, '//input[@placeholder="Search keyword"]').send_keys(category_Name)


    def ClickOnEdit(self):
        self.driver.find_element(By.XPATH, '//span[@class="p-button-icon pi pi-pen-to-square"]').click()

    def UpdateCategoryName_Field(self, Update_category_name):
        self.driver.find_element(By.XPATH, "//input[@id='category_name']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='category_name']").send_keys(Update_category_name)

    def ClickOnUpdate(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()

    def DeleteCategory(self):
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-trash']").click()

    def DeleteConfirm(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Yes')]").click()

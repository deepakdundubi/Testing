from selenium.webdriver.common.by import By
import time


class HomePage:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

    # ACTION METHODS
    def clickOnMenu(self):
        self.driver.find_element(By.XPATH, "//img[@class='p-element menu-icon']").click()

    def clickOnMasterMenu(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Master']").click()

    def navigateToMasterMenu(self):
        self.clickOnMenu()
        time.sleep(1)
        self.clickOnMasterMenu()

    def clickOnSalesMenu(self):
        self.driver.find_element(By.XPATH, "//span[text()='Sales & Marketing']").click()

    def clickOnPurchaseMenu(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Purchase']").click()

    def clickOnAccountsMenu(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Account']").click()



from selenium.webdriver.common.by import By
class LoginPage:

    # To INITILIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

        # ACTION METHODS
    def setUserName(self, username):
        self.driver.find_element(By.XPATH, "//input[@id='email']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)

    def clickSignIn(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]").click()

    def login(self, username, password):
        self.setUserName(username)
        self.setPassword(password)
        self.clickSignIn()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, '//span[@class="p-button-icon pi pi-sign-out"]').click()



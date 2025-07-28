from selenium.webdriver.common.by import By


class ProductMaster:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

    def ClickOnNew(self):
        self.driver.find_element(By.XPATH, "//span[text()='+ Add New']").click()

    def ProductType(self,Type):
        self.driver.find_element(By.XPATH, "//span[@aria-label='Select Type']").select_by_visible_text(Type)


    def ItemName(self,ItemName):
        self.driver.find_element(By.XPATH,"//input[@id='item_name']").send_keys(ItemName)

    def ItemHSN(self,ItemHSN):
        self.driver.find_element(By.XPATH,"//input[@id='hsn']").send_keys(ItemHSN)

    def ClickOnUnitsDropdown(self):
        self.driver.find_element(By.XPATH,"//span[@aria-label='Select Units']").click()
    def SearchUnit(self,EnterUnit):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(EnterUnit)
    def SelectUnit(self):
        self.driver.find_element(By.XPATH,"(//div[@class='p-element elipsis'])[1]").click()

    def ClickOnCategoryDropdown(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Select Category')]").click()
    def SearchCategory(self,EnterCategory):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(EnterCategory)
    def SelectCategory(self):
        self.driver.find_element(By.XPATH,"(//div[@class='p-element elipsis'])[1]").click()

    def ClickOnSubCategoryDropdown(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Select Sub Category')]").click()
    def SearchSubCategory(self,EnterSubCategory):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(EnterSubCategory)
    def SelectSubCategory(self):
        self.driver.find_element(By.XPATH,"(//div[@class='p-element elipsis'])[1]").click()

    def EnterPartNumber(self, PartNumber):
        self.driver.find_element(By.XPATH, "//input[@id='part_number']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='part_number']").send_keys(PartNumber)

    def EnterModel(self, Model):
        self.driver.find_element(By.XPATH, "//input[@id='model']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='model']").send_keys(Model)

    def ClickOnBrandDropdown(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Select Sub Category')]").click()
    def SearchBrand(self,EnterBrand):
        self.driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys(EnterBrand)
    def SelectBrand(self):
        self.driver.find_element(By.XPATH,"(//div[@class='p-element elipsis'])[1]").click()

    def EnterDescription(self, Description):
        self.driver.find_element(By.XPATH, "//textarea[@id='description']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys(Description)


    def EnterMRP(self, MRP):
        self.driver.find_element(By.XPATH, "//input[@id='mrp']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='mrp']").send_keys(MRP)

    def Discount_on_MRP_Sale(self,DiscountOnMrpForSale):
        self.driver.find_element(By.XPATH,"//input[@id='mrp_disc_sale']").clear()
        self.driver.find_element(By.XPATH,"//input[@id='mrp_disc_sale']").send_keys(DiscountOnMrpForSale)

    def get_sales_price(self):
        sales_price= self.driver.find_element(By.XPATH ,"//input[@id='sales_price']")
        return float(sales_price.get_attribute("value"))

    def Discount_on_MRP_Wholesale(self,DiscountOnMrpForWholeSale):
        self.driver.find_element(By.XPATH, "//input[@id='mrp_disc_wholesale']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='mrp_disc_wholesale']").send_keys(DiscountOnMrpForWholeSale)

    def get_Wholesale_price(self):
        Wholesales_price= self.driver.find_element(By.XPATH ,"//input[@id='sales_price']")
        return float(Wholesales_price.get_attribute("value"))

    def purchase_price(self,PurchasePrie):
        self.driver.find_element(By.XPATH, "//input[@id='purchase_price']").clear()
        self.driver.find_element(By.XPATH,"//input[@id='purchase_price']").send_keys(PurchasePrie)



    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, '//span[text()="Save"]').click()



from selenium.webdriver.common.by import By


class ProductMaster:
    # To INITIALIZE DRIVER
    def __init__(self, driver):
        self.driver = driver

    def ClickOnNew(self):
        self.driver.find_element(By.XPATH, "//span[text()='+ Add New']").click()

    def ProductType(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Select Type')]").click()

    def ProductTypeSearch(self, ProductTypeSearch):
        self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/input[1]").send_keys(ProductTypeSearch)

    def ProductSelectFromDropdown(self):
        self.driver.find_element(By.XPATH, "//li[@id='Type_0']").click()

    def ItemName(self,ItemName):
        self.driver.find_element(By.XPATH,"//input[@id='item_name']").send_keys(ItemName)
    def ItemHSN(self,ItemHSN):
        self.driver.find_element(By.XPATH,"//input[@id='hsn']").send_keys(ItemHSN)
    def ClickOnUnitsDropdown(self):
        self.driver.find_element(By.XPATH,"//span[@aria-label='Select Units']").click()
    def EnterUnitToSearch(self,EnterUnitToSearch):
        self.driver.find_element(By.XPATH,"//input[@id='hsn']").send_keys(EnterUnitToSearch)
    def SelectUnit(self):
        self.driver.find_element(By.XPATH,"(//div[@class='p-element elipsis'])[1]").click()



    def ProductDescription(self, ProductDescription):
        self.driver.find_element(By.XPATH, "//textarea[@id='productDetails']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='productDetails']").send_keys(ProductDescription)

    def CustomerDescription(self, CustomerDescription):
        self.driver.find_element(By.XPATH, "//textarea[@id='customerDescription']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='customerDescription']").send_keys(CustomerDescription)

    def ProductNature(self):
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Non-Hazardous')]").click()

    def ProductNatureSearch(self, ProductNatureSearch):
        # self.driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//input[@role='textbox']").send_keys(ProductNatureSearch)

    def ProductNatureSelect(self):
        self.driver.find_element(By.XPATH, "//p-dropdownitem/li").click()

    def SelectOptions(self):
        #self.driver.find_element(By.XPATH, "//p-multiselect[@display='chip']//span").clear()
        self.driver.find_element(By.XPATH, "//p-multiselect[@display='chip']//span").click()

    def SelectOptionsSearch(self, SelOptionSearch):
        self.driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[2]/input").send_keys(SelOptionSearch)

    def SelectOptionsSelect(self):
        self.driver.find_element(By.XPATH, "//p-multiselectitem/li").click()

    def SubCategory(self):
        self.driver.find_element(By.XPATH, "(//div[@aria-label='dropdown trigger'])[3]").click()

    def SubCategorySearch(self, SubCategorySearch):
        self.driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[1]/input[1]").send_keys(SubCategorySearch)

    def SubCategorySelect(self):
        self.driver.find_element(By.XPATH, "(//p-dropdownitem/li)[1]").click()

    def Category(self):
        self.driver.find_element(By.XPATH, "(//div[@aria-label='dropdown trigger'])[4]").click()

    def CategorySearch(self, CategorySearch):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/input[1]").send_keys(CategorySearch)

    def CategorySelect(self):
        self.driver.find_element(By.XPATH, "(//p-dropdownitem/li)[1]").click()

    def CreateManufacturer(self):
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon pi pi-plus']").click()

    def EnterManufacturerName(self, EnterManufacturerName):
        self.driver.find_element(By.XPATH, "//textarea[@name='GlobalValue']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@name='GlobalValue']").send_keys(EnterManufacturerName)

    def ClickOnSaveManufacturer(self):
        self.driver.find_element(By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Save'])[2]").click()

    def Manufacture(self):
        self.driver.find_element(By.XPATH, "(//div[@aria-label='dropdown trigger'])[5]").click()

    def ManufactureSearch(self, ManufactureSearch):
        self.driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[1]/input[1]").send_keys(ManufactureSearch)

    def ManufactureSelect(self):
        self.driver.find_element(By.XPATH, "(//p-dropdownitem/li)[1]").click()

    def Unit(self):
        self.driver.find_element(By.XPATH, "//div[text()='EACH']").click()

    def UnitSearch(self, UnitSearch):
        self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/input[1]").send_keys(UnitSearch)

    def UnitSelect(self):
        self.driver.find_element(By.XPATH, "//p-dropdownitem/li").click()

    def MOQ(self, MOQ):
        self.driver.find_element(By.XPATH, "//input[@id='MOQ']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='MOQ']").send_keys(MOQ)

    def ProductStatus(self):
        self.driver.find_element(By.XPATH, "(//div[@aria-label='dropdown trigger'])[7]").click()

    def ProductStatusSearch(self, ProductStatusSearch):
        self.driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH, "//body/div[2]/div[1]/div[1]/input[1]").send_keys(ProductStatusSearch)

    def ProductStatusSelect(self):
        self.driver.find_element(By.XPATH, "(//p-dropdownitem/li)[1]").click()

    def HSNcode(self, HSNcode):
        self.driver.find_element(By.XPATH, "//textarea[@id='hsnCode']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='hsnCode']").send_keys(HSNcode)

    def OBQty(self, OBQty):
        self.driver.find_element(By.XPATH, "//input[@id='obQTY']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='obQTY']").send_keys(OBQty)

    def MRP(self, MRP):
        self.driver.find_element(By.XPATH, "//input[@id='MRP']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='MRP']").send_keys(MRP)

    def TAX(self):
        self.driver.find_element(By.XPATH, "(//div[@aria-label='dropdown trigger'])[8]").click()

    def TAXSearch(self, TAXSearch):
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[11]").clear()
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[11]").send_keys(TAXSearch)

    def TAXSelect(self):
        self.driver.find_element(By.XPATH, "(//p-dropdownitem/li)[1]").click()

    def TaxRate(self, TaxRate):
        self.driver.find_element(By.XPATH, "//input[@id='TAX']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='TAX']").send_keys(TaxRate)

    def PurchasePriceExclTAX(self, PurchasePriceExclTAX):
        self.driver.find_element(By.XPATH, "//input[@id='purchasePrice']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='purchasePrice']").send_keys(PurchasePriceExclTAX)

    def SalesMargin(self, SalesMargin):
        self.driver.find_element(By.XPATH, "//input[@id='salesMargin']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='salesMargin']").send_keys(SalesMargin)

    def Weight(self, Weight):
        self.driver.find_element(By.XPATH, "//textarea[@id='weight']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='weight']").send_keys(Weight)

    def Dimension(self, Dimension):
        self.driver.find_element(By.XPATH, "//textarea[@id='Dimensions']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='Dimensions']").send_keys(Dimension)

    def SerialNumber(self, SerialNumber):
        self.driver.find_element(By.XPATH, "//textarea[@id='serialNumber']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='serialNumber']").send_keys(SerialNumber)

    def AlternateItem(self, AlternateItem):
        self.driver.find_element(By.XPATH, "//textarea[@id='alternateItem']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='alternateItem']").send_keys(AlternateItem)

    def AvailableStocks(self, AvailableStocks):
        self.driver.find_element(By.XPATH, "//input[@id='availableStock']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='availableStock']").send_keys(AvailableStocks)

    def BasicStockValue(self, BasicStockValue):
        # self.driver.find_element(By.XPATH, "//input[@id='basicStockValue']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='basicStockValue']").send_keys(BasicStockValue)

    def SafetyStockValue(self, SafetyStockValue):
        self.driver.find_element(By.XPATH, "//input[@id='safetyStockValue']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='safetyStockValue']").send_keys(SafetyStockValue)

    def MovingAveragePrice(self, MovingAveragePrice):
        self.driver.find_element(By.XPATH, "//input[@id='movingAveragePrice']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='movingAveragePrice']").send_keys(MovingAveragePrice)

    def Comments(self, Comments):
        self.driver.find_element(By.XPATH, "//textarea[@id='comments']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='comments']").send_keys(Comments)

    def ClickSAVE(self):
        self.driver.find_element(By.XPATH, "(//span[text()='Save'])[1]").click()

    def SearchProduct(self, SearchProduct):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search ...']").send_keys(SearchProduct)

    def ClickOnEdit(self):
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[9]/button[1]/span[1]").click()

    def ClickOnUpdate(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Update')]").click()

    def ClickOnDelete(self):
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[9]/button[2]").click()

    def DeleteConfirm(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Yes')]").click()

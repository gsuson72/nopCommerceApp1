import pytest
import time
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName(self, setup):  #setup is the browser to be used
        self.logger.info("***** Test_005_SearchCustomerByName")
## explain more
        self.driver = setup
        self.driver.get(self.baseURL)
## instantiate loginpage class to lp variable
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successful")
## instantiate AddCustomer class to addcust variable
        self.logger.info("***** Navigating thru Customer Link")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

    ## instantiate AddCustomer class to addcust variable
        self.logger.info("***** Starting Search Customer by Name")
        self.searchcust = SearchCustomer(self.driver)
        fname ="Arthur"
        lname ="Holmes"
        fullname = fname+" "+lname
        self.searchcust.setFirstName(fname)
        self.searchcust.setLastName(lname)
        self.logger.info(fullname)
        #self.searchcust.clickSearch()
        time.sleep(5)
        status = self.searchcust.searchCustomerByName(fullname)
        self.logger.info(status)
        if status == True:
            assert True
        else:
            assert False


















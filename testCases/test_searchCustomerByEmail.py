import pytest
import time

from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self, setup):
        self.logger.info("***** Test_004_SearchCustomerByEmail")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successful")

        self.logger.info("***** Starting Search Customer by Email")

        self.addcust = AddCustomer(self.driver)  # associating page object addcustomer
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        searchcust = SearchCustomer(self.driver)
        s_email = "steve_gates@nopCommerce.com"
        searchcust.setSEmail(s_email)

        searchcust.clickSearch() #<<<== comment out if you want to run the table coz email id is always unique

        time.sleep(5)
        status = searchcust.searchCustomerByEmail(s_email)
        self.logger.info(status)
        if status == True:
            assert True
        else:
            assert False






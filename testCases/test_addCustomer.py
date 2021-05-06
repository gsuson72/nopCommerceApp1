import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("***** Test_003_AddCustomer")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successful")
        self.logger.info("***** Starting Add Customer Test")

        self.addcust = AddCustomer(self.driver)  # associating page object addcustomer
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("***** Providing Customer Info")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        #self.addcust.setEmail("geojes12@yahoo.com")
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Jessie")

        self.addcust.setNewsletter("Test store 2")

        self.addcust.setCustomerRoles("Administrators")

        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")

        self.addcust.setLastName("Gornez")
        self.addcust.setDob("02/25/1972")
        self.addcust.setCompanyName("GeoJes")
        self.addcust.setAdminContent("This is for testing George.")
        time.sleep(3)

        self.addcust.clickOnSave()

        self.logger.info("***** Saving Customer Info")

        self.logger.info("***** Add Customer validation started")
        msg = self.driver.find_element_by_tag_name("body").text

        #print(self.msg)  # == comment out so element will not populate in the report

        if 'customer has been added successfully.' in msg:
            assert True
            self.logger.info("***** Add Customer Test Passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "addCustomer.png")
            self.logger.info("***** Add Customer Test Failed")
            self.driver.close()
            assert False



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))